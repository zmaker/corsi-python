#dizionari
listino = {"mele":12, "pere":23, "kiwi":45}

print(listino, type(listino))

#estraggo il valore di un elemento
print(listino["mele"])

#modifico
listino["mele"] = 99
print(listino)

#aggiungo
listino["fragole"] = 56
print(listino)

listino.pop("fragole")
print(listino)

#dictionary vuoto
d1 = dict()

for el in listino.keys():
    print(el, end=",")
print("")

for el in listino.values():
    print(el, end=",")
print("")

for el in listino.items():
    print(el, el[0], el[1])
    
if "mele" in listino:
    print("trovato mele")
    
listino2 = listino
print(listino)
print(listino2)
listino["mele"] = 0
print(listino)
print(listino2)

listino3 = listino.copy()
print(listino)
print(listino3)
listino["mele"] = 100
print(listino)
print(listino3)


