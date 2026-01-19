import sqlite3

conn = sqlite3.connect("pythondb.db")
cur = conn.cursor()
cur.execute("select mid, prodotto, prezzo, qta from magazzino")
for row in cur.fetchall():
    mid, prodotto, prezzo, qta = row
    print(f"{mid}: {prodotto}")

conn.close()