import sqlite3

conn = sqlite3.connect('users.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE users (
            entry_num INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL ) 
            """)

conn.commit()
conn.close()

conn = sqlite3.connect('items.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE items (
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            identifer TEXT NOT NULL,
            icon IMG,
            floor_restrict INT,
            buff INT,
            buff_for TEXT NOT NULL,
            quantity INT,
            price INT )
            """)

item_list = [
    ("Health Item I", "_", "S_MD", "image", 0, 25, "HP", 999, 999),
    ("Health Item II", "_", "S_MD", "image", 0, 25, "HP", 999, 999),
    ("Health Item III", "_", "S_MD", "image", 0, 25, "HP", 999, 999),
    ("Health Item IV", "_", "S_MD", "image", 0, 25, "HP", 999, 999),

    ("Strength Boost Item I", "_", "S_MD", "image", 0, 25, "HP", 999, 999),
    ("Strength Boost Item II", "_", "S_MD", "image", 0, 25, "HP", 999, 999),

    ("Defense Boost Item I", "_", "S_MD", "image", 0, 25, "HP", 999, 999),
    ("Defense Boost Item II", "_", "S_MD", "image", 0, 25, "HP", 999, 999),

    ("Move Scroll I", "_", "S_MD", "image", 0, 25, "HP", 999, 999),
    ("Move Scroll II", "_", "S_MD", "image", 0, 25, "HP", 999, 999),
    ("Move Scroll III", "_", "S_MD", "image", 0, 25, "HP", 999, 999),
    ("Move Scroll IV", "_", "S_MD", "image", 0, 25, "HP", 999, 999),

    ("Key II", "_", "S_MD", "image", 0, 25, "HP", 999, 999),
    ("Key III", "_", "S_MD", "image", 0, 25, "HP", 999, 999),

    ("Shady Figure Item I", "_", "S_MD", "image", 0, 25, "HP", 999, 999),
    ("Shady Figure Item II", "_", "S_MD", "image", 0, 25, "HP", 999, 999),
    ("Shady Figure Item III", "_", "S_MD", "image", 0, 25, "HP", 999, 999),

    ("Treasure Item I", "_", "S_MD", "image", 0, 25, "HP", 999, 999),
    ("Treasure Item II", "_", "S_MD", "image", 0, 25, "HP", 999, 999),
    ("Treasure Item III", "_", "S_MD", "image", 0, 25, "HP", 999, 999),
    ("Treasure Item IV", "_", "S_MD", "image", 0, 25, "HP", 999, 999),
    ("Treasure Item V", "_", "S_MD", "image", 0, 25, "HP", 999, 999),
    ("Treasure Item VI", "_", "S_MD", "image", 0, 25, "HP", 999, 999)
]

conn.commit()
conn.close()