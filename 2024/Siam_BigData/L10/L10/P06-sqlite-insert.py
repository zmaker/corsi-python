import sqlite3

conn = sqlite3.connect("pythondb.db")
cur = conn.cursor()

LOOP = True
while LOOP:
    #chiedo i dati
    mid = input("id: ")
    prodotto = input("prodotto: ")
    prezzo = input("prezzo: ")
    qta = input("qta: ")

    #compongo l'sql
    sql = f"insert into magazzino "\
    f"(mid, prodotto, prezzo, qta) values "\
    f"({mid},'{prodotto}',{prezzo},{qta})"
    print(sql)

    #inserisco nel db
    cur.execute(sql)
    conn.commit()

    #chiedo conferma prossimo insert
    ans = input("ancora? (s/n) ")
    if not (ans == 's'):
        LOOP = False


conn.close()