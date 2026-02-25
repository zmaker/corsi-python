import sqlite3

conn = sqlite3.connect("dati.db")
cur = conn.cursor()

while True:
    mid = int(input("id: "))
    nome = input("nome: ")
    prezzo = float(input("prezzo: "))
    qta = int(input("qta: "))
    
    sql = f"insert into magazzino (mid, prodotto, prezzo, qta) values "\
          f"({mid},'{nome}',{prezzo},{qta})"
    print(sql)
    
    cur.execute(sql)
    conn.commit()
    
    ans = input("ancora (s/n)? ")
    if not ans == 's':
        break

conn.close()