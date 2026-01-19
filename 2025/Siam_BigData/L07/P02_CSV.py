import csv

'''
f = open("dati.csv")
f.close()
'''
#lettura dati da file CSV
with open("dati.csv") as f:
    cur = csv.reader(f, delimiter=',')
    next(cur)
    i = 0
    for riga in cur:
        print(riga)
        print(f"codice: {riga[0]} quantità: {riga[2]}")
        i += 1

#scrittura di un file CSV
with open("magazzino.csv", "w") as f:
    cur = csv.writer(f, delimiter=',')
    cur.writerow(['cod', 'nome', 'qta', 'prz'])
    cur.writerow(['999', 'viti', 1000, 1.0])
    cur.writerow(['888', 'dadi', 1240, 0.5])