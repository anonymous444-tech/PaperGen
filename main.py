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
    
    def fetch_quiz_questions(self, subject, board, class_name):
        """
        Fetches 20 unique, randomized questions targeting all three specific 
        filter vectors directly from the database layer.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            # CRITICAL PATCH: Added ORDER BY RANDOM() to query different questions every time
            query = """
                SELECT id, question_text, option_a, option_b, option_c, option_d, correct_option 
                FROM mcq_bank 
                WHERE subject = ? AND board = ? AND class_name = ?
                ORDER BY RANDOM()
                LIMIT 20
            """
            
            cursor.execute(query, [subject, board, class_name])
            rows = cursor.fetchall()
            conn.close()
            
            questions = []
            for row in rows:
                questions.append({
                    "id": row[0],
                    "question": row[1], 
                    "options": [row[2], row[3], row[4], row[5]],
                    "correct": row[6] 
                })
            
            # Returns all 20 freshly scrambled questions across the bridge
            return json.dumps(questions)
            
        except Exception as e:
            print(f"Error reading SQLite database: {e}")
            return json.dumps([])

    def generate_and_save_paper(self, name, subject, board, class_name, chapters):
        """Trigger backend architecture generation logic and commit payload metadata into the engine db."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        try:
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


    def save_exam_completion(self, name, score, total, correct_indices_list):
        """Saves the score and flips the dashboard status to Done!"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        try:
            # 1. Update dashboard status
            cursor.execute("UPDATE generated_papers SET status = 'Done!' WHERE name = ?", (name,))
            
            # 2. Save pie chart metric data
            correct_json = json.dumps(correct_indices_list)
            cursor.execute('''
                INSERT INTO quiz_results (paper_name, score_achieved, total_questions, correct_questions_json)
                VALUES (?, ?, ?, ?)
            ''', (name, score, total, correct_json))
            
            conn.commit()
            return {"status": "success"}
        except Exception as e:
            return {"status": "error", "message": str(e)}
        finally:
            conn.close()

    def load_historical_results(self):
        """Used by result_screen.html to fetch the pie chart data"""
        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM quiz_results ORDER BY id DESC")
            rows = cursor.fetchall()
            return [dict(row) for row in rows]
        except Exception as e:
            return []
        finally:
            conn.close()

    def open_result_window(self):
        """Spins up the separate HTML window for results"""
        html_path = os.path.abspath('result_screen.html')
        webview.create_window('Exam Results', url=html_path, width=900, height=750)
        return True

def run_app():
    api = ExamEngineAPI()
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