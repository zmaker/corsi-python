import sqlite3

conn = sqlite3.connect("dati.db")
cursor = conn.cursor()

mid = int(input("id da cancellare? "))
sql = f"delete from magazzino where mid = {mid}"
print(sql)

cursor.execute(sql)
conn.commit()    

conn.close()


