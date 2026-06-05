import csv

with open("dati.csv") as f:
    rows = csv.reader(f, delimiter=",")
    for riga in rows:
        print(riga)