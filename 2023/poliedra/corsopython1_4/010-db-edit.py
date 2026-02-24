import sqlite3

conn = sqlite3.connect("dati.db")
cursor = conn.cursor()

mid = int(input("id? "))
qta = int(input("qta? "))
sql = f"update magazzino set qta={qta} where mid = {mid}"
print(sql)

cursor.execute(sql)
conn.commit()    

conn.close()

