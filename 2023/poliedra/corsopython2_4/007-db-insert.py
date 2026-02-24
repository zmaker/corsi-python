import sqlite3

c = sqlite3.connect("magazzino.db")
cur = c.cursor()

while True:
    nome = input("frutta: ")
    qta = int(input("qta: "))
    prz = float(input("prz: "))
    
    sql = f"insert into frutta (nome, qta, prezzo) values "\
          f"('{nome}',{qta},{prz})"
    
    print(sql)
    cur.execute(sql)
    c.commit()

    ans = input("ancora (s/n)? ")
    if not ans == 's':
        break
    
c.close()
