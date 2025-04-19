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