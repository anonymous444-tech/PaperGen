import os
import sqlite3
import json
import webview

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