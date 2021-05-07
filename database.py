import sqlite3


class AccountDatabase:

    def __init__(self, database: str = "accounts.sqlite"):
        self._db = database
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS accounts (
                              id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                              login TEXT NOT NULL,
                              password TEXT NOT NULL);""")
            connection.commit()
        connection.close()

    def get_account(self):
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            result = cursor.execute("""SELECT id, login, password
                                       FROM accounts""").fetchall()
        return result

    def add_new_account(self, id_, login, password) -> bool:
        pass

    def change_password(self, account_id, new_password) -> bool:
        pass

    def change_login(self, account_id, new_login) -> bool:
        pass
