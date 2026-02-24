import sqlite3

conn = sqlite3.connect("dati.db")
cursor = conn.cursor()
cursor.execute("select * from magazzino")

for row in cursor.fetchall():
    print(f"({row[0]}) - {row[1]} p={row[2]} q={row[3]}")
    

conn.close()