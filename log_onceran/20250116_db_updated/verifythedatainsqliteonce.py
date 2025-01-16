import sqlite3

conn = sqlite3.connect("history.db")
c = conn.cursor()

c.execute("SELECT * FROM historical_figures LIMIT 10")  # Check first 10 rows
rows = c.fetchall()

for row in rows:
    print(row)

conn.close()
