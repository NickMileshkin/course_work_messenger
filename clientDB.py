import sqlite3


class ClientDatabase:

    def __init__(self, database: str = "ClientDB.sqlite"):
        self._db = database
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS dialogs (
                              dialog_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                              account_id INTEGER NOT NULL);""")
            cursor.execute("""CREATE TABLE IF NOT EXISTS messages (
                              message_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                              account_id INTEGER NOT NULL,
                              dialog_id INTEGER NOT NULL,
                              time INTEGER NOT NULL,
                              message TEXT NOT NULL,
                              is_new BOOLEAN NOT NULL);""")
            connection.commit()
        connection.close()

    def get_dialogs(self):
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            result = cursor.execute("""SELECT dialog_id, account_id
                                       FROM dialogs""").fetchall()
        return result
