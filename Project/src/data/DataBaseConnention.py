import sqlite3
from pathlib import Path



class DataBaseConnentionClass():
    
    def __init__(self):
        self.db_path: Path = Path(__file__).parent.parent.parent / "database" / "chatbot_data.sqlite"
        self.db_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

    def get_connection(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON;")

        return conn
    
    def close(self, conn: sqlite3.Connection):
        if conn:
            conn.close()

