import sqlite3
import time

class DatabaseConnection:
    def __init__(self, db_name='Youtube_videos.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS videos(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                time TEXT NOT NULL,
                video_link TEXT NOT NULL,
                created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at DATETIME NULL
            )
        ''')
        self.conn.commit()

    def list_all_videos(self):
        self.cursor.execute("SELECT * FROM videos")
        rows = self.cursor.fetchall()
        return rows

    def add_video(self, name, time_, video_link):
        self.cursor.execute(
            "INSERT INTO videos (name, time, video_link) VALUES (?, ?, ?)",
            (name, time_, video_link)
        )
        self.conn.commit()

    def update_video(self, id_, name, time_, video_link):
        current_timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.cursor.execute(
            "UPDATE videos SET name = ?, time = ?, video_link = ?, updated_at = ? WHERE id = ?",
            (name, time_, video_link, current_timestamp, id_)
        )
        self.conn.commit()

    def delete_video(self, id_):
        self.cursor.execute("DELETE FROM videos WHERE id = ?", (id_,))
        self.conn.commit()

    def check_video(self, name, time_):
        self.cursor.execute(
            "SELECT name, time FROM videos WHERE name = ? AND time = ?",
            (name, time_)
        )
        return self.cursor.fetchone()

    def close(self):
        self.conn.close()
