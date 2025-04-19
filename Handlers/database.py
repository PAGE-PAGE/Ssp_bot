import sqlite3 as sq


def db_start():
    with sq.connect("sspaper.db") as db:
        cursor = db.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS users ('
                       'user_id INTEGER PRIMARY KEY,'
                       'referrer_id INTEGER,'
                       'username TEXT,'
                       'wins INTEGER,'
                       'draw INTEGER,'
                       'loses INTEGER,'
                       'bonuses INTEGER)')
        db.commit()


def user_in(id: int, name: str = None, ref_id: int = None):
    with sq.connect("sspaper.db") as db:
        try:
            cursor = db.cursor()
            cursor.execute('INSERT INTO users(user_id, username, referrer_id) VALUES (?,?,?)', (id, name, ref_id))
            db.commit()
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


def gun(id: int):
    with sq.connect("sspaper.db") as db:
        cursor = db.cursor()
        cursor.execute('SELECT wins, loses, draw FROM users WHERE user_id = ?', (id,))
        return cursor.fetchall()


def get_friends(id: int):
    with sq.connect("sspaper.db") as db:
        cursor = db.cursor()
        cursor.execute('SELECT COUNT(referrer_id) FROM users WHERE referrer_id = ?', (id,))
        results = cursor.fetchall()
        results = results[0][0]
        return results


def get_bonuses(id: int):
    with sq.connect("sspaper.db") as db:
        cursor = db.cursor()
        cursor.execute('SELECT bonuses FROM users WHERE user_id = ?', (id,))
        results = cursor.fetchall()
        results = results[0][0]
        return results


def check_for_bonus(id: int):
    with sq.connect("sspaper.db") as db:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM users WHERE user_id = ?', (id,))
        results = cursor.fetchall()
        results = results[0][1]
        if results is not None:
            cursor.execute('UPDATE users SET bonuses = COALESCE(bonuses, 0) + 1 WHERE user_id = ?', (results,))
            db.commit()

# ¯\_(ツ)_/¯
