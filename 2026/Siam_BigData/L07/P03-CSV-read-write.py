import csv

with open("dati.csv") as f:
    rows = csv.reader(f, delimiter=",")
    l = next(rows)
    print(l)
    print()
    for riga in rows:
        #print(riga)
        print(f"cod: {riga[0]} - {riga[1]} qtà: {riga[2]}")