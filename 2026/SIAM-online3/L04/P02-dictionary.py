# dizionari - key:valore
listino = { "X01":"mela", "X02":"pera", "P99":"kiwi" }
anagrafica = { "LVAGFSGFHSFHSFH":"Mario Rossi", "GFDGFH45L34GDHGDH":"Luigi Bianchi" }
magazzino = {"chiodi":123, "viti":345, "bulloni":456}

#creo un dizionario vuoto
elenco = dict()

#estraggo un valore
print( listino["X02"] )
print( listino.get("X01") )

#modifico un elemento
listino["X02"] = "fragola"
print(listino)

#aggiunta
listino["P01"] = "ananas"
print(listino)

#verifico se un elemento è presente
if "P99" in listino:
    print("trovato")

#rimuovere elementi - pop() genera errore se elemento non presente
if "P012" in listino:
    listino.pop("P012")
print(listino)

del listino["X01"]
print(listino)

#svuoto il dictionary
listino.clear()
print(listino)

#scorrere elementi di un dictionary
mag = {"mele":12, "pere":23, "kiwi":34}
print(mag.keys())

for k in mag.keys():
    print(k, mag[k])

for el in mag.values():
    print(el)

for el in mag.items():
    chiave, valore = el #unpacking della tupla
    print("k:", chiave, " = ", valore)

# comportamenti strani dei dizionari
magazzino2 = magazzino
print("m1", magazzino)
print("m2", magazzino2)

magazzino["chiodi"] = 0
print("m1 . 1", magazzino)
print("m2 . 1", magazzino2)

magazzino3 = magazzino.copy()
magazzino["chiodi"] = 1000
print("m1 . 2", magazzino)
print("m3 . 2", magazzino3)

