import sqlite3
import pytest


@pytest.fixture
def test_connection():
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE messages(
            id TEXT PRIMARY KEY,
            prompt TEXT,
            role TEXT,
            time TEXT
        )
    """)

    conn.commit()

    yield conn

    conn.close()