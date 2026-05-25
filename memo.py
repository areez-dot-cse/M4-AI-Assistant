import sqlite3
connection = sqlite3.connect("memory.db")
cursor=connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS memories(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
               thing text,
               place text)""")
connection.commit()

def remember(thing, place):
    cursor.execute(
        "INSERT INTO memories (thing,place) VALUES (?,?)", (thing, place)
    )
    connection.commit()
    act=f"I will remember that {thing} is in {place}"
    return act

def recall(thing):
    thing=thing.lower()
    cursor.execute(
        "SELECT place, created_at FROM memories WHERE thing = ?", (thing,)
    )
    result=cursor.fetchone()

    if result:
        tt = result[1].split(" ")[0]
        act = f"You placed {thing} at {result[0]} on {tt}"
    else:
        act=f"I dont remember where you kept {thing}"
    return act

