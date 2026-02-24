lista = [1,2,3]
tupla1 = (42, 45, 99)
tupla2 = (1, "Hello", 3.4)

print(tupla1)

for el in tupla2:
    print(el)
    
print(tupla1[1])

print(len(tupla1))

tupla3 = ("A", "B", "C", "A", "D")
print(tupla3.count("A"))

#packing/unpacking
var1 = 10, "mele", 1.98
print(var1)

a, b, c = var1
print("a:", a)
print("b:", b)
print("c:", c)

#cerco un elemento
pos = tupla3.index("B")
print("pos= ", pos)

print ("A" in tupla3)
print ("X" in tupla3)

print(tupla1 * 2)
