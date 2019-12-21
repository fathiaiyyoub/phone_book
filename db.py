

import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS phone_book (id INTEGER PRIMARY KEY, first_name text , last_name text, phone_number INTEGER)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM phone_book")
        rows = self.cur.fetchall()
        return rows

    def insert(self, first_name, last_name, phone_number):
        self.cur.execute("INSERT INTO phone_book VALUES (NULL, ?, ?, ?)",
                         (first_name, last_name, phone_number))
        self.conn.commit()

    def delete(self, id):
        self.cur.execute("DELETE FROM phone_book WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, first_name, last_name, phone_number):
        self.cur.execute("UPDATE phone_book SET 'first_name' = ?, last_name = ?, phone_number = ? WHERE id = ?",
                         (first_name, last_name, phone_number, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

db = Database('phone_book.db')


	