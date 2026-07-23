import sqlite3
from Project.src.models.Message import MessageClass

from pathlib import Path

class MessageDAOClass():
    
    def __init__(self, connection):
        # Az adatbázisod fix útvonala
        self.db_path: Path = Path(__file__).parent.parent.parent / "database" / "chatbot_data.sqlite"
        self.conn: sqlite3.Connection  = connection


    def save_message(self, message: MessageClass) -> bool:

        if (message == None):
            print("Nincsen üzenet")
            return False
        
        try:
            cur = self.conn.cursor()

            cur.execute(
                """
                INSERT INTO messages(id, prompt, role, time) VALUES(?, ?, ?, ?)
                """,
                    (
                        message.id,
                        message.prompt,
                        message.role,
                        message.time,
                    )
            )

            
            self.conn.commit()

            return True

        except Exception as e:
            print("ELeve baj van")
            print("DB error:", e)
            return False

    def get_message_count(self) -> int:
        """Megszámolja, hány üzenet van jelenleg az adatbázisban."""


        try:
            cursor = self.conn.cursor()

            cursor.execute(
                "SELECT COUNT(*) FROM messages;",
            )
            return cursor.fetchone()[0]

        
        except Exception as e:
            print(f"DAO ERROR (Számlálás): {e}")
            return 0
        finally:
            if 'cursor' in locals():
                cursor.close()


    def get_all_messages(self) -> MessageClass:
        """Lekéri az összes üzenetet időrendben a memóriához."""


        try:
            cursor = self.conn.cursor()

            cursor.execute(
                "SELECT id, role, prompt, time FROM messages ORDER BY time ASC;"
            )
           
            rows =  cursor.fetchall()

            messages = []

            for row in rows:
                messages.append(
                MessageClass(
                    id=row["id"],
                    prompt=row["prompt"],
                    role=row["role"],
                    time=row["time"]
                    )
                )

            return messages
        
        except Exception as e:
            print(f"DAO ERROR (Lekérés): {e}")
            return []
        finally:
            if 'cursor' in locals():
                cursor.close()


    def clear_messages_and_set_summary(self, message: MessageClass):
        """Kitörli a régi üzeneteket, és berakja az új összefoglalót első elemnek."""

        if(message == None):
            return

        try:
            cursor = self.conn.cursor()

            # 1. törlés
            
            cursor.execute(
                "DELETE FROM messages;"
            )
            # 2. Az összefoglalót mint egy Rendszerüzenetet (System) vagy asszisztenst mentjük el


            cursor.execute(
                """
                INSERT INTO messages (id, prompt, role, time) VALUES (?, ?, ?, ?);
                """,
                ( 
                    message.id,
                    message.prompt,
                    message.role,
                    message.time,
                )
            )
            self.conn.commit()
            print("DAO INFO: Adatbázis sikeresen tömörítve az összefoglalóval!")
        except Exception as e:
            print(f"DAO ERROR (Tömörítés): {e}")
        finally:
            if 'cursor' in locals():
                cursor.close()

