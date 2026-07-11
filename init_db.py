import sqlite3

def init_database():
    conn = sqlite3.connect('exam_engine.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS generated_papers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            subject TEXT NOT NULL,
            board TEXT NOT NULL,
            class_name TEXT NOT NULL,
            chapters TEXT NOT NULL,
            status TEXT DEFAULT 'Pending'
        )
    ''')

 
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT NOT NULL,
            chapter TEXT NOT NULL,
            type TEXT NOT NULL,           -- MCQ (1m), SA (3m), LA (5m)
            marks INTEGER NOT NULL,
            question_text TEXT NOT NULL,
            answer_hint TEXT
        )
    ''')

    seed_questions = [
        # --- PHYSICS ---
        ('Physics', 'Force, Work, Power & Energy', 'MCQ', 1, 'A body of mass 2 kg falls from a height of 10m. Calculate the potential energy lost.', 'PE = mgh = 2 * 9.8 * 10 = 196 J'),
        ('Physics', 'Force, Work, Power & Energy', 'LA', 5, 'State the law of conservation of energy and prove it mathematically for a freely falling body.', 'Show PE+KE=Constant at top, middle, and bottom points of fall.'),
        ('Physics', 'Light & Spectrum', 'SA', 3, 'Explain the phenomenon of total internal reflection. State two necessary conditions for it to occur.', '1. Light must travel from denser to rarer medium. 2. Angle of incidence > critical angle.'),
        ('Physics', 'Electricity & Magnetism', 'MCQ', 1, 'Which instrument is used to detect the presence of a weak electric current in a circuit?', 'Galvanometer'),

        # --- CHEMISTRY ---
        ('Chemistry', 'Acids, Bases & Salts', 'MCQ', 1, 'What is the color change observed when blue litmus paper is dipped in an acidic solution?', 'It turns red.'),
        ('Chemistry', 'Chemical Bonding', 'SA', 3, 'Compare electrovalent (ionic) compounds and covalent compounds based on their melting points and electrical conductivity.', 'Ionic have high MP and conduct in molten/aqueous state. Covalent have low MP and do not conduct.'),
        ('Chemistry', 'Organic Chemistry', 'LA', 5, 'Define homologous series. State its four core characteristics and write the structural formula of ethanoic acid.', 'Series with same functional group, diff by -CH2-. Characteristics: similar chemical properties, grading physical properties.'),

        # --- MATHEMATICS ---
        ('Mathematics', 'Commercial Algebra (GST)', 'SA', 3, 'A shopkeeper buys an article for ₹1000 and sells it to a consumer at a profit of 20%. If the GST rate is 18%, calculate the total GST paid by the consumer.', 'Selling Price = ₹1200. GST = 1200 * 18% = ₹216.'),
        ('Mathematics', 'Algebra & Quadratic Equations', 'LA', 5, 'Solve the quadratic equation for x using the quadratic formula: 2x² - 7x + 3 = 0.', 'x = [7 ± √(49 - 24)] / 4 => x = 3 or x = 0.5.'),

        # --- COMPUTER ---
        ('Computer', 'Object Oriented Programming', 'MCQ', 1, 'Which OOP principle acts as a mechanism to bind data and code together into a single unit?', 'Encapsulation'),
        ('Computer', 'String Handling', 'SA', 3, 'Write a Java expression to check if a given String variable "str" ends with the character code substring "Gen".', 'str.endsWith("Gen")'),

        # --- BIOLOGY ---
        ('Biology', 'Cell Division & Chromosomes', 'MCQ', 1, 'During which phase of mitosis do the chromosomes align along the equatorial plane of the spindle?', 'Metaphase'),
        ('Biology', 'Circulatory System', 'LA', 5, 'Describe the double circulation process in the human heart with the help of structural tracking concepts.', 'Explain systemic and pulmonary circulation loops separately.')
    ]


    cursor.execute("DELETE FROM questions")
    cursor.executemany('''
        INSERT INTO questions (subject, chapter, type, marks, question_text, answer_hint)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', seed_questions)

    conn.commit()
    print(f"Database ready! Embedded {cursor.rowcount} tailored sample questions mapped directly to your JS schema.")
    conn.close()

if __name__ == '__main__':
    init_database()