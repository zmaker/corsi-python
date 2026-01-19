import sqlite3

conn = sqlite3.connect("pythondb.db")
cur = conn.cursor()

mid = 2
sql = f"update magazzino set qta = 999 where mid = {mid}"
cur.execute(sql)
conn.commit()

conn.close()

