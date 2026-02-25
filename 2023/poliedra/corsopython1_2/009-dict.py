listino = {"mele":12, "pere":10, "kiwi":8}
print(listino)

#dizionario vuoto
rubrica = dict()

print("n mele: ", listino["mele"])
print("n mele: ", listino.get("mele"))

listino["mele"] = 99
print("n mele: ", listino["mele"])

for kk in listino.keys():
    print(kk)

for vv in listino.values():
    print(vv)
    
for el in listino.items():
    print(el)

print("mele?", "mele" in listino)
print("mango?", "mango" in listino)

listino["mango"] = 100
print(listino)

#rimuovo elementi
listino.pop("mango")
print(listino)
#popitem()

listino["mango"] = 100
del listino["mango"]
print("con del", listino)

#svuoto dict
listino.clear()
#del listino
print("clear", listino)

#copia
listino2 = {"mele":12, "pere":10, "kiwi":8}
l3 = listino2
print("l2", listino2)
print("l3", l3)

l3["mele"]=99

print("l2", listino2)
print("l3", l3)

l4 = listino2.copy()
l4["mele"]=100
print("l2", listino2)
print("l4", l4)

