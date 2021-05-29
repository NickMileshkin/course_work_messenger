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

    def get_accounts(self):
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            result = cursor.execute("""SELECT id, login, password
                                       FROM accounts""").fetchall()
        return result

    def add_new_account(self, login, password) -> bool:
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO accounts (login, password)
                              VALUES (?, ?)""", (login, password))
            connection.commit()

    def get_authorization(self, login, password) -> bool:
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            account = cursor.execute("""SELECT id FROM accounts WHERE login = ? AND
                                        password = ?""", (login, password)).fetchone()
        return True if account is not None else False

    def change_password(self, account_id, new_password) -> bool:
        pass

    def change_login(self, account_id, new_login) -> bool:
        pass
