frutta = ["mela", "pera", "fragola", "banana"]
mag    = [100,       120,       200,       75]

qta_totale = 0
qta_media = 0

#stampo il contenuto del mio magazzino
indice = 0
for prodotto in frutta:
    print((indice+1), prodotto, mag[indice], sep="\t")
    #aggiungo la quantità corrente a qta_totale
    qta_totale = qta_totale + mag[indice]
    #indice = indice + 1
    indice += 1
    
print("qta totale: ", qta_totale)
qta_media = qta_totale / len(mag)
print("qta media: ", qta_media)