import sqlite3

conn = sqlite3.connect("dati.db")
cursor = conn.cursor()

mid = int(input("id? "))
sql = f"select * from magazzino where mid = {mid}"
print(sql)

cursor.execute(sql)

for row in cursor.fetchall():
    print(f"({row[0]}) - {row[1]} p={row[2]} q={row[3]}")
    

conn.close()
