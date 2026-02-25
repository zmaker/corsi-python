import sqlite3

c = sqlite3.connect("magazzino.db")
cur = c.cursor()

fid = int(input("id del record: "))

qta = int(input("qta: "))
    
sql = f"update frutta set qta = {qta} where fid = {fid}"
print(sql)

cur.execute(sql)
c.commit()
 
c.close()

