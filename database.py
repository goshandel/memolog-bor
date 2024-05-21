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
        self.cursor.execute("""SELECT id FROM users
                             WHERE id = ?""",
                            (id,))
        data = self.cursor.fetchone()
        return data is not None

    def add_user(self, id, user_name, nickname):
        self.cursor.execute("INSERT INTO users VALUES(?,?,?,?,?,?,?,?);",
                            (id, user_name, nickname, None, None, None, 'False', None))
        self.connect.commit()

    def add_year(self, id, year):
        self.cursor.execute("UPDATE users SET year =? WHERE id =?", (year, id))
        self.connect.commit()

    def add_month(self, id, month):
        self.cursor.execute("UPDATE users SET month =? WHERE id =?", (month, id))
        self.connect.commit()

    def get_year_month(self, id):
        self.cursor.execute("SELECT month, year FROM users WHERE id =?", (id,))
        results = self.cursor.fetchall()
        formatted_results = [{"year": row[1], "month": row[0]} for row in results]
        combined_results = []
        for result in formatted_results:
            combined_result = f"{result['year']}/{result['month']}"
            combined_results.append(combined_result)
        return combined_results

    def check_admin(self, id):
        self.cursor.execute("SELECT admin FROM users WHERE id =?", (id,))
        results = self.cursor.fetchall()
        if results:
            result = results[0][0]
            if result == "True":
                return True
            elif result == "False":
                return False
            else:
                raise ValueError(f"Unexpected value '{result}' in admin column")
        else:
            return None

    def new_admin(self, id):
        self.cursor.execute("UPDATE users SET admin =? WHERE id =?", ('True', id,))
        self.connect.commit()

    def add_meme(self, id, meme):
        self.cursor.execute("UPDATE users SET meme =? WHERE id =?", (meme, id))
        self.connect.commit()

    def add_council(self, id, council):
        self.cursor.execute("UPDATE users SET council =? WHERE id =?", (council, id))
        self.connect.commit()

    def get_council(self, id):
        result = self.cursor.execute("SELECT council FROM users WHERE id =?", (id,))
        row = result.fetchone()
        if row is None:
            return False
        else:
            return row[0]

    def close(self):
        self.connect.close()


class Years_base:
    def __init__(self):
        self.connect = sqlite3.connect('years.db')
        self.cursor = self.connect.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS years 
                        (year_month TEXT PRIMARY KEY AUTOINCREMENT,
                        memes TEXT,
                        edit_meme TEXT)""")
        self.connect.commit()

    def add_new_month(self, year_month):
        self.cursor.execute("INSERT INTO years VALUES(?,?,?);",
                            (year_month, None, None))
        self.connect.commit()

    def add_meme(self, year_month, meme):
        self.cursor.execute("UPDATE years SET memes = CONCAT(memes,?, '\n') WHERE year_month =?",
                            (meme, year_month))
        self.connect.commit()

    def get_edit_meme(self, year_month):
        result = self.cursor.execute("SELECT edit_meme FROM years WHERE year_month = ?", (year_month))
        row = result.fetchone()
        if row is None:
            return False
        else:
            return row[0]

    def add_edit_meme(self, year_month, edit_meme):
        self.cursor.execute("SELECT edit_meme FROM years WHERE year_month =?", (year_month,))
        result = self.cursor.fetchone()

        if result is None or result[0] == '':
            self.cursor.execute("UPDATE years SET edit_meme =? WHERE year_month =?", (edit_meme, year_month))
            self.connect.commit()
            return True
        else:
            return False
