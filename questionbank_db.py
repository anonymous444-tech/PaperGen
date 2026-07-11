import sqlite3

def questionbank_db():
    conn = sqlite3.connect('exam_engine.db')
    cursor = conn.cursor()

    # 1. Create the MCQ Question Bank table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mcq_bank (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
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

    # 2. Comprehensive Question Bank mapped EXACTLY to your JS Strings
    mcq_data = [
        # ==================== PHYSICS ====================
        ('Physics', 'Force, Work, Power & Energy', 'What is the SI unit of work and energy?', 'Watt', 'Joule', 'Newton', 'Pascal', 'B'),
        ('Physics', 'Light & Spectrum', 'Which of the following is a necessary condition for Total Internal Reflection?', 'Light travels from rarer to denser medium', 'Light travels from denser to rarer medium', 'Angle of incidence is less than critical angle', 'Refractive index must be equal to 1', 'B'),
        ('Physics', 'Sound Waves', 'What is the audible frequency range for a normal human ear?', '20 Hz to 20,000 Hz', '2 Hz to 200 Hz', '20 kHz to 20 MHz', 'Less than 20 Hz only', 'A'),
        ('Physics', 'Electricity & Magnetism', 'Which law states that the direction of induced current always opposes the cause producing it?', 'Ohm\'s Law', 'Coulomb\'s Law', 'Lenz\'s Law', 'Ampere\'s Law', 'C'),
        ('Physics', 'Heat & Thermodynamics', 'The heat energy required to change the state of a substance without a change in temperature is called:', 'Specific heat capacity', 'Latent heat', 'Heat capacity', 'Calorific value', 'B'),
        ('Physics', 'Modern Physics', 'Which type of radiation has the highest ionizing power?', 'Alpha particles', 'Beta particles', 'Gamma rays', 'X-Rays', 'A'),

        # ==================== CHEMISTRY ====================
        ('Chemistry', 'Periodic Properties', 'Moving down a group in the periodic table, the electron affinity generally:', 'Increases', 'Decreases', 'Remains the same', 'First increases then decreases', 'B'),
        ('Chemistry', 'Chemical Bonding', 'What type of chemical bond is formed by the complete transfer of electrons from one atom to another?', 'Covalent bond', 'Coordinate bond', 'Electrovalent (Ionic) bond', 'Metallic bond', 'C'),
        ('Chemistry', 'Acids, Bases & Salts', 'What is the use of SG bottle?', 'for gravity', 'for RD', 'for measurement', 'for volume', 'B'),
        ('Chemistry', 'Analytical Chemistry', 'What color precipitate is formed when Sodium Hydroxide solution is added to Ferrous Sulfate solution?', 'Chalky white', 'Dirty green', 'Reddish brown', 'Pale blue', 'B'),
        ('Chemistry', 'Mole Concept', 'What is the number of atoms present in one mole of any substance (Avogadro\'s number)?', '6.022 x 10^22', '6.022 x 10^23', '3.14 x 10^23', '9.1 x 10^-31', 'B'),
        ('Chemistry', 'Metallurgy', 'Which of the following is the chief ore of Aluminum metal?', 'Hematite', 'Bauxite', 'Galena', 'Calamine', 'B'),
        ('Chemistry', 'Organic Chemistry', 'What is the general formula for the homologous series of Alkanes?', 'C_n H_2n', 'C_n H_2n-2', 'C_n H_2n+2', 'C_n H_2n+1', 'C'),

        # ==================== COMPUTER ====================
        ('Computer', 'Object Oriented Programming', 'Which OOP principle acts as a mechanism to bind data and code together into a single structural unit?', 'Inheritance', 'Polymorphism', 'Encapsulation', 'Abstraction', 'C'),
        ('Computer', 'User-Defined Methods', 'Which return type is used when a method does not return any value to the calling context?', 'int', 'float', 'void', 'String', 'C'),
        ('Computer', 'Constructors & Overloading', 'A constructor has the exact same name as its:', 'Package', 'Class', 'Object', 'Return type', 'B'),
        ('Computer', 'Library Classes', 'Which standard package automatically imports itself into every Java compilation unit?', 'java.util', 'java.io', 'java.lang', 'java.net', 'C'),
        ('Computer', 'Encapsulation & Arrays', 'What is the index value of the first structural element stored inside a standard array matrix?', '1', '-1', '0', 'Depends on array size', 'C'),
        ('Computer', 'String Handling', 'What is the output evaluated by the Java string structure execution: "Engine".charAt(3)?', 'E', 'n', 'g', 'i', 'D'),

        # ==================== BIOLOGY ====================
        ('Biology', 'Cell Division & Chromosomes', 'During which structural phase of mitosis do chromosomes align uniformly along the equatorial plane?', 'Prophase', 'Metaphase', 'Anaphase', 'Telophase', 'B'),
        ('Biology', 'Plant Physiology & Transpiration', 'The loss of water in the form of liquid droplets along the margins of leaves via specialized structures is known as:', 'Transpiration', 'Guttation', 'Photosynthesis', 'Evaporation', 'B'),
        ('Biology', 'Circulatory System', 'Which specific blood vessel carries deoxygenated blood away from the heart directly into the lungs?', 'Aorta', 'Pulmonary Vein', 'Pulmonary Artery', 'Superior Vena Cava', 'C'),
        ('Biology', 'Excretory System', 'What constitutes the foundational structural and functional unit of the human kidney?', 'Nephron', 'Neuron', 'Alveoli', 'Liver lobe', 'A'),
        ('Biology', 'Nervous System', 'Which sector of the human brain is explicitly responsible for managing body balance, posture, and muscular coordination?', 'Cerebrum', 'Cerebellum', 'Medulla Oblongata', 'Pons', 'B'),
        ('Biology', 'Endocrine & Genetics', 'A deficiency in the secretion of which hormone directly triggers the onset of Diabetes Mellitus?', 'Thyroxine', 'Adrenaline', 'Insulin', 'Growth Hormone', 'C'),

        # ==================== MATHEMATICS ====================
        ('Mathematics', 'Commercial Algebra (GST)', 'In an intra-state business transaction, the Goods and Services Tax collected is shared equally between:', 'Central Govt and Union Territory', 'Central Govt (CGST) and State Govt (SGST)', 'Two different state governments', 'Manufacturer and Wholesaler', 'B'),
        ('Mathematics', 'Algebra & Quadratic Equations', 'What is the nature of the roots of a quadratic equation if its Discriminant (D) evaluates exactly to 0?', 'Real and Distinct', 'Real and Equal', 'Imaginary / No Real Roots', 'Negative and Irrational', 'B'),
        ('Mathematics', 'Geometry & Circles', 'An angle subtended by a diameter semicircle arc at any point on the remaining circumference of a circle is always:', '45 degrees', '60 degrees', '90 degrees', '180 degrees', 'C'),
        ('Mathematics', 'Trigonometry', 'What does the fundamental trigonometric identity statement expression sin²θ + cos²θ evaluate to?', '0', '1', '2', '-1', 'B'),
        ('Mathematics', 'Mensuration', 'What is the formula representing the total volume capacity space of a standard cylinder shape?', 'πr²h', '1/3 πr²h', '2πrh', '4/3 πr³', 'A'),
        ('Mathematics', 'Statistics & Probability', 'What is the strict mathematical value assigned to the probability metric of an absolutely impossible event instance occurring?', '1', '0.5', '0', '-1', 'C')
    ]

    # Clean old instances out to prevent duplicate keys during testing iteration loops
    cursor.execute("DROP TABLE IF EXISTS mcq_bank")
    cursor.execute('''
        CREATE TABLE mcq_bank (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
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

    cursor.executemany('''
        INSERT INTO mcq_bank (subject, chapter, question_text, option_a, option_b, option_c, option_d, correct_option)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', mcq_data)

    conn.commit()
    print(f"SQLite Data Bank Loaded Successfully! Committed {cursor.rowcount} premium matching MCQs.")
    conn.close()

if __name__ == '__main__':
    questionbank_db()