import sqlite3
with sqlite3.connect("database.db") as c:
    cur = c.cursor()
    mid, prodotto, prezzo, qta = (8, 'mokabon', 4.5, 123)
    sql = f"insert into coffee "\
        f"(cid, name, price, qty) values "\
        f"( {mid}, '{prodotto}', {prezzo}, {qta} )"
    print(sql)
    cur.execute(sql)
    c.commit()
