import sqlite3


class AccountDatabase:

    def __init__(self, database: str = "MessengerDB.sqlite"):
        self._db = database
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS accounts (
                              account_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                              login TEXT NOT NULL,
                              password TEXT NOT NULL);""")
            cursor.execute("""CREATE TABLE IF NOT EXISTS dialogs (
                              dialog_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                              user1_id INTEGER NOT NULL,
                              user2_id INTEGER NOT NULL);""")
            cursor.execute("""CREATE TABLE IF NOT EXISTS messages (
                              message_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                              account_id INTEGER NOT NULL,
                              dialog_id INTEGER NOT NULL,
                              time TEXT NOT NULL,
                              message TEXT NOT NULL,
                              is_new BOOLEAN NOT NULL);""")
            connection.commit()
        connection.close()

    def get_account_info(self, account_id):
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            result = cursor.execute("""SELECT login FROM accounts WHERE account_id = ?""",
                                    (account_id,)).fetchone()
        if result is None:
            return False
        else:
            return result[0]

    def add_new_account(self, login, password):
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO accounts (login, password)
                              VALUES (?, ?)""", (login, password))
            connection.commit()

    def get_authorization(self, login, password) -> bool:
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            account = cursor.execute("""SELECT account_id FROM accounts WHERE login = ? AND
                                        password = ?""", (login, password)).fetchone()
        if account is not None:
            return account[0]
        else:
            return False

    def change_password(self, account_id, new_password):
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            cursor.execute("""UPDATE accounts SET password = ? WHERE account_id = ?""",
                           (new_password, account_id))
            connection.commit()

    def change_login(self, account_id, new_login):
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            cursor.execute("""UPDATE accounts SET login = ? WHERE account_id = ?""",
                           (new_login, account_id))
            connection.commit()

    def check_password(self, account_id, password) -> bool:
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            check = cursor.execute("""SELECT password FROM accounts WHERE account_id = ?""",
                                   (account_id,)).fetchone()[0]
        if check == password:
            return True
        else:
            return False

    def create_new_dialog(self, user1_id, user2_id) -> bool:
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            check1 = cursor.execute("""SELECT dialog_id FROM dialogs WHERE user1_id = ? AND user2_id = ?""",
                                    (user1_id, user2_id)).fetchone()
            check2 = cursor.execute("""SELECT dialog_id FROM dialogs WHERE user2_id = ? AND user1_id = ?""",
                                    (user1_id, user2_id)).fetchone()
            check3 = cursor.execute("""SELECT account_id FROM accounts WHERE account_id = ? OR account_id = ?""",
                                    (user1_id, user2_id)).fetchall()
            if (check1 is not None) or (check2 is not None) or (len(check3) < 2):
                return False
            else:
                cursor.execute("""INSERT INTO dialogs (user1_id, user2_id)
                                  VALUES (?, ?)""", (user1_id, user2_id))
                connection.commit()
                result = cursor.execute("""SELECT dialog_id FROM dialogs WHERE user1_id = ? AND user2_id = ?""",
                                        (user1_id, user2_id)).fetchone()[0]
                return result

    def send_message(self, account_id, dialog_id, time, message):
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO messages (account_id, dialog_id, time, message, is_new)
                              VALUES (?, ?, ?, ?, ?)""", (account_id, dialog_id, time, message, True))
            connection.commit()

    def get_all_messages(self, user_id):
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            dialogs = cursor.execute("""SELECT dialog_id FROM dialogs WHERE user1_id = ? OR user2_id = ?""",
                                     (user_id, user_id)).fetchall()
            messages = []
            if len(dialogs) > 0:
                for i in range(len(dialogs)):
                    messages += cursor.execute("""SELECT account_id, dialog_id, time, message, is_new FROM messages 
                                                  WHERE dialog_id = ?""", (dialogs[i][0],)).fetchall()
            return messages

    def get_new_messages(self, user_id):
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            dialogs = cursor.execute("""SELECT dialog_id FROM dialogs WHERE user1_id = ? OR user2_id = ?""",
                                     (user_id, user_id)).fetchall()
            messages = []
            if len(dialogs) > 0:
                for i in range(len(dialogs)):
                    messages += cursor.execute("""SELECT account_id, dialog_id, time, message FROM messages 
                                                  WHERE dialog_id = ? AND is_new = ?""",
                                               (dialogs[i][0], True)).fetchall()
            return messages

    def get_dialogs(self, user_id):
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            dialogs = cursor.execute("""SELECT dialog_id, user1_id FROM dialogs 
                                        WHERE user2_id = ?""", (user_id,)).fetchall()
            dialogs += cursor.execute("""SELECT dialog_id, user2_id FROM dialogs 
                                         WHERE user1_id = ?""", (user_id,)).fetchall()
            return dialogs

    def read_this_dialog(self, dialog_id, account_id):
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            cursor.execute("""UPDATE messages SET is_new = ? WHERE dialog_id = ? AND account_id != ?""",
                           (False, dialog_id, account_id))
            connection.commit()
