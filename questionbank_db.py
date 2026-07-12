import sqlite3

def questionbank_db():
    conn = sqlite3.connect('exam_engine.db')
    cursor = conn.cursor()

    # Drop old configuration to avoid alignment mutations
    cursor.execute("DROP TABLE IF EXISTS mcq_bank")
    
    # Create aligned schema matching the 10-column data array tuple layout
    cursor.execute('''
        CREATE TABLE mcq_bank (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            board TEXT NOT NULL,
            class_name TEXT NOT NULL,
            subject TEXT NOT NULL,
            chapter TEXT NOT NULL,
            question_text TEXT NOT NULL,
            option_a TEXT NOT NULL,
            option_b TEXT NOT NULL,
            option_c TEXT NOT NULL,
            option_d TEXT NOT NULL,
            correct_option TEXT NOT NULL
        )
    ''')

    # SEED DATA: 20 COMPLETELY DISTINCT, UNIQUE QUESTIONS FOR THE TARGET CATEGORY
    mcq_data = [
        # ==================== CBSE - CLASS 10 - PHYSICS (20 UNIQUE QUESTIONS) ====================
        ('CBSE', 'Class 10', 'Physics', 'Light Reflection', 'The focal length of a spherical mirror of radius of curvature R is:', 'R', 'R / 2', '2R', '3R', 'B'),
        ('CBSE', 'Class 10', 'Physics', 'Light Reflection', 'A concave mirror gives virtual, erect, and magnified image when the object is placed:', 'At F', 'Between F and C', 'Beyond C', 'Between P and F', 'D'),
        ('CBSE', 'Class 10', 'Physics', 'Light Reflection', 'The refractive index of transparent medium is maximum for which color?', 'Red', 'Yellow', 'Green', 'Violet', 'D'),
        ('CBSE', 'Class 10', 'Physics', 'Light Reflection', 'The power of a lens is -2.0 D. What is its focal length and lens type?', '-50cm, concave', '-50cm, convex', '-20cm, concave', '-20cm, convex', 'A'),
        ('CBSE', 'Class 10', 'Physics', 'Human Eye', 'The deflection of light by minute particles and molecules in the atmosphere is called:', 'Dispersion', 'Scattering', 'Interference', 'Total Internal Reflection', 'B'),
        ('CBSE', 'Class 10', 'Physics', 'Human Eye', 'The change in focal length of an eye lens is caused by the action of the:', 'Pupil', 'Retina', 'Ciliary muscles', 'Iris', 'C'),
        ('CBSE', 'Class 10', 'Physics', 'Human Eye', 'A person cannot see distinctly objects kept beyond 2m. This defect can be corrected by using a lens of power:', '-0.5 D', '+0.5 D', '-0.2 D', '+0.2 D', 'A'),
        ('CBSE', 'Class 10', 'Physics', 'Electricity', 'The SI unit of electrical resistivity is:', 'Ohm', 'Ohm-meter', 'Volt/meter', 'Ohm/meter', 'B'),
        ('CBSE', 'Class 10', 'Physics', 'Electricity', 'How much work is done in moving a charge of 2 C across two points having a potential difference 12 V?', '6 J', '24 J', '0.16 J', '14 J', 'B'),
        ('CBSE', 'Class 10', 'Physics', 'Electricity', 'When three resistors of 2 ohms, 4 ohms, and 6 ohms are connected in parallel, the equivalent resistance is:', 'Less than 2 ohms', 'Exactly 12 ohms', 'Greater than 6 ohms', 'Exactly 4 ohms', 'A'),
        ('CBSE', 'Class 10', 'Physics', 'Electricity', 'Joule heating effect equation is mathematically represented as:', 'H = V / I', 'H = I * R * t', 'H = I² * R * t', 'H = V² * R * t', 'C'),
        ('CBSE', 'Class 10', 'Physics', 'Magnetic Effects', 'The magnetic field lines inside a long current-carrying straight solenoid are:', 'Circular', 'Zero', 'Parabolic', 'Parallel straight lines', 'D'),
        ('CBSE', 'Class 10', 'Physics', 'Magnetic Effects', 'The device used for producing electric current is called a:', 'Generator', 'Galvanometer', 'Ammeter', 'Motor', 'A'),
        ('CBSE', 'Class 10', 'Physics', 'Magnetic Effects', 'An alpha particle projected towards west is deflected towards north by a magnetic field. The direction of magnetic field is:', 'Towards south', 'Towards east', 'Downward', 'Upward', 'D'),
        ('CBSE', 'Class 10', 'Physics', 'Magnetic Effects', 'The phenomenon of electromagnetic induction is:', 'Charging a body', 'Producing induced current due to relative motion', 'Rotating an electric motor coil', 'Generating a magnetic field around a wire', 'B'),
        ('CBSE', 'Class 10', 'Physics', 'Light Reflection', 'An object is placed at a distance of 10 cm in front of a convex mirror of focal length 15 cm. Find the image distance:', '6 cm', '-6 cm', '30 cm', '-30 cm', 'A'),
        ('CBSE', 'Class 10', 'Physics', 'Light Reflection', 'A full-length image of a distant tall building can definitely be seen by using:', 'A concave mirror', 'A convex mirror', 'A plane mirror', 'Both concave and plane mirror', 'B'),
        ('CBSE', 'Class 10', 'Physics', 'Light Reflection', 'Magnification produced by a rear view mirror fitted in vehicles:', 'Is less than one', 'Is more than one', 'Is equal to one', 'Can be more or less than one', 'A'),
        ('CBSE', 'Class 10', 'Physics', 'Electricity', 'What is the relationship between the heat produced H and current I according to Joules Law?', 'H proportional to I', 'H proportional to I²', 'H proportional to 1/I', 'H proportional to 1/I²', 'B'),
        ('CBSE', 'Class 10', 'Physics', 'Magnetic Effects', 'At the time of short circuit, the current in the circuit:', 'Reduces substantially', 'Does not change', 'Increases heavily', 'Varies continuously', 'C')
    ]

    # Bulk insert the truly unique datasets safely
    cursor.executemany('''
        INSERT INTO mcq_bank (board, class_name, subject, chapter, question_text, option_a, option_b, option_c, option_d, correct_option)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', mcq_data)

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS quiz_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            paper_name TEXT NOT NULL,
            score_achieved INTEGER NOT NULL,
            total_questions INTEGER NOT NULL,
            correct_questions_json TEXT NOT NULL, 
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    print(f"🚀 SQLite Data Bank Loaded Successfully! Seeded {cursor.rowcount} REAL unique reference rows.")
    conn.close()

if __name__ == '__main__':
    questionbank_db()