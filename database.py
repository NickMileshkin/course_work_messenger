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

    def add_new_account(self, login, password):
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
        if account is not None:
            return account[0]
        else:
            return False

    def change_password(self, account_id, new_password):
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            cursor.execute("""UPDATE accounts SET password = ? WHERE id = ?""",
                           (new_password, account_id))
            connection.commit()

    def change_login(self, account_id, new_login):
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            cursor.execute("""UPDATE accounts SET login = ? WHERE id = ?""",
                           (new_login, account_id))
            connection.commit()


class MessageDatabase:

    def __init__(self, database: str = "messages.sqlite"):
        self._db = database
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS messages (
                              id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                              sender TEXT NOT NULL,
                              recipient TEXT NOT NULL,
                              time INTEGER NOT NULL,
                              message TEXT NOT NULL);""")
            connection.commit()
        connection.close()

    def send_message(self, sender, recipient, time, message):
        pass

    def synchronization(self, login):
        pass
