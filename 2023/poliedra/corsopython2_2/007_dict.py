d1 = dict()
print(d1)

d2 = {"mele":12,\
      "pere":23, "kiwi":56}
print(d2)

print(d2["mele"])

d2["mele"] = 99
print(d2["mele"])
print(d2.get("mele"))

for k in d2.keys():
    print("k:", k)

for v in d2.values():
    print("v:", v)
    
for el in d2.items():
    print("it:", el)
    
print("banane" in d2)
print("mele" in d2)

d2["banane"] = 100
print(d2)

d2.popitem()
print(d2)

d2.pop("pere")
print(d2)

del d2["kiwi"]
print(d2)

#del d2
d2.clear()

d3 = {"mele":12, "pere":23, "kiwi":56}
d4 = d3

d4["mele"] = 99
print("d3: ", d3)
print("d4: ", d4)

d5 = d3.copy()
d6 = dict(d3)

d5["mele"] = 200
print("d3: ", d3)
print("d5: ", d5)



