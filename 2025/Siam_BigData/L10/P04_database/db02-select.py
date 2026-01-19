import sqlite3

with sqlite3.connect("database.db") as c:
    #interrogo la tabella coffee
    sql = "select * from coffee"
    #creo un cursore = oggetto che punta alle righe dalla tabella coffee
    cur = c.cursor()
    #eseguo la query
    cur.execute(sql)

    for row in cur.fetchall():
        print(row)

