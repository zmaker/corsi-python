#stampare il numero di oggetti in magazzino e il valore totale della merce

import csv

quantita_totale = 0
valore_totale_merce = 0

with open("dati.csv") as f:
    #creo il cursore per leggere i dati riga per riga 
    cur = csv.reader(f, delimiter=',')
    #salto la prima riga con le intestazioni
    next(cur)
    #scorro le rige una a una
    for riga in cur:
        #print(riga)
        #estraggo la quantità dalla riga corrente
        qta = int(riga[2])
        print(qta)
        #sommo la quantità della riga alla qtà totale
        quantita_totale += qta
        #estraggo il prezzo
        prz = float(riga[3])
        #sommo il valore parziale
        valore_totale_merce += prz * qta
    
print("qtà totale:", quantita_totale)
print("val. tot. magazzino:", valore_totale_merce)
