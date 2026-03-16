# Esercizio - CSV -> SQL
# Leggo i dati da un file CSV e li copio in una tabella di database
import sqlite3
import csv

# nome del file da importare
filename = "vendite.csv"
#nome del database
dbname = "vendite.db"
#nome tabella dati
tablename = "vendite"

def main():
    with sqlite3.connect(dbname) as conn:

        #creo la tabella se necessario
        sql = f"CREATE TABLE IF NOT EXISTS {tablename} ("\
        f"rid INTEGER PRIMARY KEY AUTOINCREMENT, "\
        f"cod TEXT, qta INTEGER, prz REAL"\
        f")"
        cur = conn.cursor()
        cur.execute(sql)

        #svuoto la tabella
        sql = f"DELETE FROM {tablename}"
        cur.execute(sql)

        conn.commit()

        #apro il file e lo leggo
        with open(filename) as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(row)
                prod = row["codice_prodotto"]
                qta = row["qta"]
                prz = row["prezzo"]

                sql = f"INSERT INTO {tablename} (cod, qta, prz) "\
                    f"VALUES ('{prod}',{qta}, {prz})"

                cur.execute(sql)
            conn.commit()


if __name__ == '__main__':
    main()