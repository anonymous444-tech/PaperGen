import os
import sqlite3
import json
import webview
import random

class ExamEngineAPI:
    def __init__(self):
        self.db_name = 'exam_engine.db'

    def fetch_saved_papers(self):
        """Query SQLite and return all historical papers to build the dashboard row structure dynamically."""
        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM generated_papers ORDER BY id DESC")
            rows = cursor.fetchall()
            return [dict(row) for row in rows]
        except Exception as e:
            return {"error": str(e)}
        finally:
            conn.close()
    
    def fetch_quiz_questions(self, subject):
        """
        Fetches relevant rows cleanly from the matching mcq_bank table
        and transforms them into the payload schema expected by the frontend.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            # Target the correct table (mcq_bank) and correct column name (question_text)
            query = "SELECT id, question_text, option_a, option_b, option_c, option_d, correct_option FROM mcq_bank WHERE subject = ?"
            
            cursor.execute(query, [subject])
            rows = cursor.fetchall()
            conn.close()
            
            # Map structural database rows to the clean array configuration your UI expects
            questions = []
            for row in rows:
                questions.append({
                    "id": row[0],
                    "question": row[1], # Maps 'question_text' field directly to JS 'question' key
                    "options": [row[2], row[3], row[4], row[5]],
                    "correct": row[6] 
                })
            
            # Randomize items to simulate an organic testing canvas environment
            random.shuffle(questions)
            selected_questions = questions[:10] # Cap engine feed limit to 10 items
            
            return json.dumps(selected_questions)
            
        except Exception as e:
            print(f"Error reading SQLite database: {e}")
            return json.dumps([])

    def generate_and_save_paper(self, name, subject, board, class_name, chapters):
        """Trigger backend architecture generation logic and commit payload metadata into the engine db."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        try:
            # Convert python list to string to store flatly inside SQLite field
            chapters_str = json.dumps(chapters)
            
            cursor.execute('''
                INSERT INTO generated_papers (name, subject, board, class_name, chapters, status)
                VALUES (?, ?, ?, ?, ?, 'Pending')
            ''', (name, subject, board, class_name, chapters_str))
            
            conn.commit()
            return {"status": "success", "message": "Paper record committed locally!"}
        except Exception as e:
            return {"status": "error", "message": str(e)}
        finally:
            conn.close()

def run_app():
    api = ExamEngineAPI()
    
    # Target your template directly in the local folder block
    html_path = os.path.abspath('graphics.html')
    
    window = webview.create_window(
        title='PaperGen Engine Workspace', 
        url=html_path, 
        js_api=api,
        width=1000,
        height=750,
        resizable=True
    )
    webview.start(debug=True)

if __name__ == '__main__':
    run_app()