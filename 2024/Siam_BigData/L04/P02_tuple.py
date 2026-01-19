frutta = ("mela", "pera", "banana")
print(frutta[1])

costanti = ("CODICEX", 100, 3.14, "password")

for el in frutta:
    print(el)
    
print(len(frutta))

print(type(frutta))

lettere = ("A", "B", "A", "C", "A", "D")
print(lettere.count("A"))

if "A" in lettere:
    print("A è presente")
    
#lettere.append("X")

a = (1, 2, 3)
b = (4, 5)
c = a + b
print(c)

print(type(c))

print(a * 2)

#packing/unpacking
dati = ("mela", 100, 1.98)
print(dati)
a, b, c = dati
print(a)
print(b)
print(c)


