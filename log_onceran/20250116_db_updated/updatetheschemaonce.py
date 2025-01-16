import sqlite3

# Connect to the database
conn = sqlite3.connect("history.db")
c = conn.cursor()

# Modify the table to include parent_id (if it does not exist)
c.execute('''
    CREATE TABLE IF NOT EXISTS historical_figures (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        birth_year INTEGER,
        birth_place TEXT,
        lat REAL,
        lon REAL,
        link TEXT,
        story TEXT,
        parent_id INTEGER,
        FOREIGN KEY (parent_id) REFERENCES historical_figures(id)
    )
''')

conn.commit()
conn.close()
print("Database schema updated successfully.")
