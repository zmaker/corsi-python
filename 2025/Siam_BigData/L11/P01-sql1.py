import sqlite3

somma = 0
with sqlite3.connect("database.db") as c:
    cur = c.cursor()
    cur.execute("select * from coffee")
    for row in cur.fetchall():
        somma += int(row[2])
        print(row)
print("somma:", somma)