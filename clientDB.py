import sqlite3


class ClientDatabase:

    def __init__(self, database: str = "ClientDB.sqlite"):
        self._db = database
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS dialogs (
                              dialog_id INTEGER NOT NULL PRIMARY KEY,
                              account_id INTEGER NOT NULL);""")
            cursor.execute("""CREATE TABLE IF NOT EXISTS messages (
                              message_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                              account_id INTEGER NOT NULL,
                              dialog_id INTEGER NOT NULL,
                              time TEXT NOT NULL,
                              message TEXT NOT NULL,
                              is_new BOOLEAN NOT NULL);""")
            connection.commit()
        connection.close()

    def is_authorization(self):
        pass

    def authorization(self):
        pass

    def get_dialogs(self):
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            result = cursor.execute("""SELECT dialog_id, account_id
                                       FROM dialogs""").fetchall()
        return result

    def add_dialog(self, dialog_id, account_id):
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO dialogs (dialog_id, account_id)
                              VALUES (?, ?)""", (dialog_id, account_id))
            connection.commit()

    def add_message(self, account_id, dialog_id, time, message, is_new):
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO messages (account_id, dialog_id, time, message, is_new)
                              VALUES (?, ?, ?, ?, ?)""", (account_id, dialog_id, time, message, is_new))
            connection.commit()

    def get_messages(self, dialog_id):
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            messages = cursor.execute("""SELECT account_id, time, message, is_new FROM messages 
                                                  WHERE dialog_id = ?""", (dialog_id,)).fetchall()
            return messages

    def read_this_dialog(self, dialog_id):
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            cursor.execute("""UPDATE messages SET is_new = ? WHERE dialog_id = ?""",
                           (False, dialog_id))
            connection.commit()
