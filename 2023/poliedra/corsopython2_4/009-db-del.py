import sqlite3

c = sqlite3.connect("magazzino.db")
cur = c.cursor()

fid = int(input("id del record da cancellare: "))

ans = input("sicuro (s/n)? ")
if ans == 's':
    
    sql = f"delete from frutta where fid = {fid}"
    print(sql)

    cur.execute(sql)
    c.commit()
 
c.close()


