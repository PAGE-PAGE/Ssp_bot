import sqlite3 as sq


def db_start():
    with sq.connect("sspaper.db") as db:
        cursor = db.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS users ('
                       'user_id INTEGER PRIMARY KEY,'
                       'username TEXT,'
                       'wins INTEGER,'
                       'draw INTEGER,'
                       'loses INTEGER)')
        db.commit()


def user_in(id: int, name: str = ''):
    with sq.connect("sspaper.db") as db:
        try:
            cursor = db.cursor()
            cursor.execute('INSERT INTO users(user_id, username) VALUES (?,?)', (id, name))
            db.commit()
        except sq.IntegrityError:
            print(f"User with user_id {id} already created")
        except Exception as e:
            print(f":Error while adding new user {e}")


def win_counter(id: int):
    with sq.connect("sspaper.db") as db:
        cursor = db.cursor()
        cursor.execute('UPDATE users SET wins = COALESCE(wins, 0) +1 WHERE user_id = ?', (id,))
        db.commit()


def loses_counter(id: int):
    with sq.connect("sspaper.db") as db:
        cursor = db.cursor()
        cursor.execute('UPDATE users SET loses = COALESCE(loses, 0) +1 WHERE user_id = ?', (id,))
        db.commit()


def draw_counter(id: int):
    with sq.connect("sspaper.db") as db:
        cursor = db.cursor()
        cursor.execute('UPDATE users SET draw = COALESCE(draw, 0) +1 WHERE user_id = ?', (id,))
        db.commit()


def gpd_wld(id: int):
    with sq.connect("sspaper.db") as db:
        cursor = db.cursor()
        cursor.execute('SELECT username, wins, loses, draw FROM users WHERE user_id = ?', (id,))
        return cursor.fetchall()


def gun(username: str):
    with sq.connect("sspaper.db") as db:
        cursor = db.cursor()
        cursor.execute('SELECT wins, loses, draw FROM users WHERE username = ?', (username,))
        return cursor.fetchall()

# ¯\_(ツ)_/¯
