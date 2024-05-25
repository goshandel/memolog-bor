import sqlite3
import io

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
        if results and results[0][0] is not None and results[0][1] is not None:
            year, month = results[0]
            formatted_result = f"{year}{month}"
            return formatted_result
        else:
            return None

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

    def get_meme(self, id):
        result = self.cursor.execute("SELECT meme FROM users WHERE id = ?", (id,))
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
                        (year_month INTEGER PRIMARY KEY AUTOINCREMENT,
                        memes TEXT,
                        edit_meme TEXT)""")
        self.connect.commit()

    def add_new_month(self, year_month):
        self.cursor.execute("INSERT INTO years (year_month, memes, edit_meme) VALUES (?, ?, ?)",
                            (year_month, "", ""))
        self.connect.commit()

    def check_year_month(self, year_month):
        self.cursor.execute("""SELECT year_month FROM years WHERE year_month = ?""", (year_month,))
        data = self.cursor.fetchone()
        return data is not None

    def get_meme(self, year_month):
        result = self.cursor.execute("SELECT memes FROM years WHERE year_month = ?", (year_month,))
        row = result.fetchone()
        if row is None:
            return False
        else:
            return row[0]

    def add_meme(self, year_month, meme):
        result = self.cursor.execute("SELECT memes FROM years WHERE year_month =?", (year_month,))
        row = result.fetchone()
        if row is not None:
            if isinstance(row[0], str):
                new_memes = row[0] + '' + meme
            else:
                new_memes = str(row[0]) + '' + meme
            self.cursor.execute("UPDATE years SET memes =? WHERE year_month =?", (new_memes, year_month))
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

    def close(self):
        self.connect.close()

class Memes_base:
    def __init__(self):
        self.connect = sqlite3.connect('memes.db')
        self.cursor = self.connect.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS memes 
                        (num INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        description TEXT,
                        photo TEXT)""")
        self.connect.commit()

    def add_new_meme(self, name):
        self.cursor.execute("INSERT INTO memes (name, description, photo) VALUES (?,?,?)", (name, "", ""))
        self.connect.commit()

    def add_description(self, description, name):
        self.cursor.execute("UPDATE memes SET description = ? WHERE name =?",
                            (description, name))
        self.connect.commit()

    def add_photo(self, photo, name):
        self.cursor.execute("UPDATE memes SET photo = ? WHERE name = ?",
                            (photo, name))
        self.connect.commit()

    def get_photo(self, name):
        self.cursor.execute("SELECT photo FROM memes WHERE name = ?", (name,))
        row = self.cursor.fetchone()
        print(row)
        if row is None:
            return False
        else:
            return row[0]

    def get_description(self, name):
        self.cursor.execute("SELECT description FROM memes WHERE name = ?", (name,))
        row = self.cursor.fetchone()
        print(row)
        if row is None:
            return False
        else:
            return row[0]

    def close(self):
        self.connect.close()

# описание, выбрать мем, предложка

def image_to_base64(image_path):
    img = Image.open(image_path)
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    base64_str = base64.b64encode(img_byte_arr).decode('utf-8')

    return base64_str

def string_to_base64(input_string):
    # Преобразование строки в байтовую последовательность
    byte_arr = input_string.encode('utf-8')
    # Кодирование байтовой последовательности в Base64
    base64_str = base64.b64encode(byte_arr).decode('utf-8')
    return base64_str


import base64
from PIL import Image
from io import BytesIO


def decode_base64_image(base64_string):
    assert isinstance(base64_string, str), "base64_string must be a string"
    if "data:image" in base64_string:
        base64_string = base64_string.split(",")[1]
    image_bytes = base64.b64decode(base64_string)
    image_stream = BytesIO(image_bytes)
    image = Image.open(image_stream)

    return image