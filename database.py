import sqlite3


class Users_base:
    def __init__(self):
        self.connect = sqlite3.connect('users.db')
        self.cursor = self.connect.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users 
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_name TEXT,
                        nickname TEXT,
                        year INTEGER, 
                        month TEXT,
                        meme TEXT,
                        admin TEXT,
                        council TEXT)""")
        self.connect.commit()

    def check_user_exists(self, id):
        self.cursor.execute("""SELECT id FROM speak
                             WHERE id = ?""",
                            (id,))
        data = self.cursor.fetchone()
        return data is not None

    def add_user(self, id, user_name, nickname):
        self.cursor.execute("INSERT INTO speak VALUES(?,?,?,?,?,?,?,?);",
                            (id, user_name, nickname, 0, '', '', 'False', ''))
        self.connect.commit()