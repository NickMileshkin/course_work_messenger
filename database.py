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

    def check_password(self, account_id, password) -> bool:
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            check = cursor.execute("""SELECT password FROM accounts WHERE id = ?""",
                                   (account_id,)).fetchone()[0]
        if check == password:
            return True
        else:
            return False


class MessageDatabase:

    def __init__(self, database: str = "messages.sqlite"):
        self._db = database
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS messages (
                              id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                              sender_id INTEGER NOT NULL,
                              recipient_id INTEGER NOT NULL,
                              time INTEGER NOT NULL,
                              message TEXT NOT NULL,
                              is_new BOOLEAN NOT NULL);""")
            connection.commit()
        connection.close()

    def send_message(self, sender_id, recipient_id, time, message):
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO messages (sender_id, recipient_id, time, message, is_new)
                              VALUES (?, ?, ?, ?, ?)""", (sender_id, recipient_id, time, message, True))
            connection.commit()

    def synchronization(self, user_id):
        pass

    def get_new_messages(self, user_id):
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            new_msg = cursor.execute("""SELECT sender_id, time, message, FROM messages 
                                        WHERE recipient_id = ? AND is_new = ?""",
                                        (user_id, True)).fetchall()
            print(new_msg)
