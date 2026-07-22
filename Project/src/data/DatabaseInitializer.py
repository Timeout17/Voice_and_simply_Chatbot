import sqlite3


class DatabaseInitializerClass():

    def __init__(self, conn):
        self.conn = conn

    def CreateMessagetable(self):
        try:
            cur = self.conn.cursor()
            
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS messages(
                    id TEXT PRIMARY KEY,
                    prompt TEXT,
                    role TEXT,
                    time NUMERIC
                );
                """
            )

            self.conn.commit()
        except sqlite3.Error as e:
            print(e)
            # itt lesz még loggolás