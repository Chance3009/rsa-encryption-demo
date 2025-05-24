# Database
import sqlite3


class MessageDatabase:
    def __init__(self, db_name="messages.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.initialize_database()

    def initialize_database(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS encrypted_messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                encrypted_text TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()

    def save_message(self, encrypted_text):
        self.cursor.execute(
            'INSERT INTO encrypted_messages (encrypted_text) VALUES (?)',
            (encrypted_text,)
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def get_message_by_id(self, message_id):
        self.cursor.execute(
            'SELECT * FROM encrypted_messages WHERE id = ?', (message_id,))
        return self.cursor.fetchone()

    def get_all_messages(self):
        self.cursor.execute('SELECT * FROM encrypted_messages')
        return self.cursor.fetchall()

    def __del__(self):
        self.conn.close()
