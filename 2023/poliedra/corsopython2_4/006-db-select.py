import sqlite3

c = sqlite3.connect("magazzino.db")
cur = c.cursor()
cur.execute("select * from frutta")

for row in cur.fetchall():
    print(f"({row[0]}) {row[1]} p:{row[2]} q:{row[3]}")

c.close()