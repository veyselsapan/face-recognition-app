# Manages a database to store and retrieve the embeddings and labels (names or IDs) of known individuals. 
# Includes functions to add new faces, retrieve faces for recognition, and delete faces.

import sqlite3

class DatabaseManager:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        """
        Create a table to store face embeddings and labels.
        """
        query = '''CREATE TABLE IF NOT EXISTS faces (
                       id INTEGER PRIMARY KEY,
                       label TEXT NOT NULL,
                       embedding BLOB NOT NULL
                   );'''
        self.conn.execute(query)
        self.conn.commit()

    def add_face(self, label, embedding):
        """
        Add a new face embedding and label to the database.
        """
        query = 'INSERT INTO faces (label, embedding) VALUES (?, ?)'
        self.conn.execute(query, (label, embedding))
        self.conn.commit()

    def get_all_faces(self):
        """
        Retrieve all face embeddings and labels from the database.
        """
        cursor = self.conn.execute('SELECT label, embedding FROM faces')
        return cursor.fetchall()

    def close(self):
        self.conn.close()
