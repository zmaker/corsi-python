# Tuple
frutta = ('mele', 'pere', 'kiwi')
print(frutta)
print(frutta[0])

for el in frutta:
    print(el, end=' ')
print("")

print(len(frutta))

#frutta[0] = 'fragole'
#frutta.append("pomelo")

costanti = ("java", 100, 1.45)
print(costanti)

#packing/unpacking
a, b, c = costanti
print(a)
print(b)
print(c)

dati = "a", 3, 45
print(dati)

#verificare se un valore è presente nella tupla
if ("java" in costanti):
    print("presente nella tupla")
else:
    print("non trovato")

if ("moka" in costanti):
    print("presente nella tupla")
else:
    print("non trovato")
    
t = (1, 2, 3)
p = (10, 20)
print(t+p)

print(t*3)



