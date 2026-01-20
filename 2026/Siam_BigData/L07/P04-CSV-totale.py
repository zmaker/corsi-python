import csv

# numero totale pezzi
tot_item = 0
# valore economico totale del magazzino
tot_mag = 0

with open("dati.csv") as f:
    rows = csv.reader(f, delimiter=",")
    #salto la prima riga - header
    l = next(rows)
    #scorro le righe del file
    for riga in rows:
        print(riga)
        qta = int(riga[2])
        prz = float(riga[3])
        print(qta, prz)

        tot_item += qta
        tot_mag += qta * prz
        #print(f"cod: {riga[0]} - {riga[1]} qtà: {riga[2]}")

print("tot pezzi: ", tot_item)
print("tot mag: ", tot_mag)
print("prz medio: ", tot_mag/tot_item)
