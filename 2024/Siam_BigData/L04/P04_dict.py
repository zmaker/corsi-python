listino = {"mele":12, "pere":23, "kiwi":45}
print(listino, type(listino))

print(listino["mele"])
print(listino.get("mele"))

listino["mele"] = 35
print(listino)

listino["fragole"] = 99
print(listino)

listino.pop("fragole")
print(listino)

#del listino["kiwi"]
#print(listino)

d1 = dict()

print("lista chiavi")
for el in listino.keys():
    print(el, end=" ")

print("\n\nlista valori")
for el in listino.values():
    print(el, end=" ")

print("\n\nlista items")
for el in listino.items():
    print(el, el[0], el[1])
    
listino2 = listino.copy()
