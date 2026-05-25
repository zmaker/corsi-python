#tupla
frutta = ("mele", "pere", "kiwi")
print(frutta)
print( frutta[0] )
# frutta[0] = 'patata'
print("numero di elementi:", len(frutta))

costanti = ("www.google.com", 123, 8080, 1.45)

for el in frutta:
    print(el)

for i, el in enumerate(frutta):
    print(i, el)

# packing/unpacking
prodotto = ("moka", 100, 1.23)
a, b, c = prodotto #unpacking
print(a)
print(b)
print(c)

#packing
n = 99
dati = "a", 123, 4.56, "fragole", n
print(dati)

#verificare se un elemento è presente nella tupla
if "fragole" in dati:
    print("si")
else:
    print("no")
    
#operazioni con le tupleì
t = (1,2,3)
p = (10,20)
print( t+p )

print( t*3 )


