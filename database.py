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
        formatted_results = []
        for row in results:
            if row[0] is not None and row[1] is not None:
                formatted_results.append(f"{row[1]}_{row[0]}")
            else:
                formatted_results.append(None)
        return formatted_results

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

    def update_and_return_council(self):
        select_query = "SELECT id, council FROM users WHERE council IS NOT NULL LIMIT 1"
        cursor = self.cursor.execute(select_query)
        row = cursor.fetchone()

        if row is not None:
            user_id, current_council = row
            update_query = "UPDATE users SET council =? WHERE id =?"
            self.cursor.execute(update_query, (None, user_id))
            self.connect.commit()
            return current_council
        else:
            return None

    def get_all_users(self):
        self.cursor.execute("SELECT * FROM users")
        results = self.cursor.fetchall()
        return results

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


class Memes_base:
    def __init__(self):
        self.connect = sqlite3.connect('memes.db')
        self.cursor = self.connect.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS memes 
                        (name TEXT PRIMARY KEY AUTOINCREMENT,
                        description TEXT,
                        photo TEXT)""")
        self.connect.commit()

    def add_new_meme(self, name):
        self.cursor.execute("INSERT INTO memes VALUES(?,?,?);",
                            (name, None, None))
        self.connect.commit()

    def add_description(self, description, name):
        self.cursor.execute("UPDATE memes SET description = ? WHERE name =?",
                            (description, name))
        self.connect.commit()

    def add_photo(self, photo, name):
        self.cursor.execute("UPDATE memes SET photo = ? WHERE name =?",
                            (photo, name))

    def get_photo(self, name):
        result = self.cursor.execute("SELECT photo FROM memes WHERE name = ?", (name))
        row = result.fetchone()
        if row is None:
            return False
        else:
            return row[0]

    def get_description(self, name):
        result = self.cursor.execute("SELECT description FROM memes WHERE name = ?", (name))
        row = result.fetchone()
        if row is None:
            return False
        else:
            return row[0]

# описание, выбрать мем, предложка

