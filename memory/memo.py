import sqlite3
import os

BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.join(BASE_DIR, "memory.db")

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS memories(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    thing TEXT,
    place TEXT
)
""")
connection.commit()


def remember(thing, place):
    thing = thing.lower()
    place = place.lower()
    cursor.execute(
        "INSERT INTO memories (thing, place) VALUES (?, ?)",
        (thing, place)
    )
    connection.commit()
    act = f"I will remember that {thing} is in {place}"
    return act


def recall(thing):
    thing = thing.lower()
    cursor.execute(
        """
        SELECT place, created_at
        FROM memories
        WHERE thing = ?
        ORDER BY id DESC
        LIMIT 1
        """,
        (thing,)
    )
    result = cursor.fetchone()
    if result:
        date = result[1].split(" ")[0]
        act = f"You placed {thing} at {result[0]} on {date}"
    else:
        act = f"I dont remember where you kept {thing}"
    return act