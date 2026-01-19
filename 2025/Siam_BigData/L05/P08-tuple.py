# tuple (liste read-only)

frutta = ("mela", "pera", "kiwi")

print(frutta)
print(frutta[1])
for el in frutta:
    print(el, end=" ")
    
print("")

#frutta.append("fragola") ERRORE! Non posso aggiungere

#packing/unpacking
dati = ("mela", 100, 1.98)
a, b, c = dati
print(a)
print(b)
print(c)

def calc(n, m):
    s = n + m
    p = n * m
    return s, p

somma, prodotto = calc(10,20)
print(somma)
print(prodotto)