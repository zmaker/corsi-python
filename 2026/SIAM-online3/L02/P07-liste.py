#liste in python

numeri = [12, 23, 43, 45, 67, 78]
print(numeri)
lista_vuota = []
print(lista_vuota)

print( len(numeri) )

print( numeri[0] )
print( numeri[3] )
print( numeri[5] )
# print( numeri[6] ) #errore!! sono uscito dalla lista

numeri[0] = 99
print(numeri)

#aggiungere un elemento alla lista
numeri.append(89)
print(numeri, len(numeri))

#lista con tipi differenti
mag = ["mele", 120, 0.98, "pere", 100, 2.34, "kiwi", 200, 3.45]
print(mag)

#estrarre un elemento
numeri.pop()
print(numeri)

n = numeri.pop()
print(n)

#rimuovere un elemento
nomi = ["luigi", "silvia", "marco", "max"]
print(nomi)
nomi.remove("marco")
print(nomi)

if "simon" in nomi:
    nomi.remove("simon")
else:
    print("non trovato")

#slicing
#   | 0|  1|  2|  3|  4|  5|  6|  7|
n = [12, 23, 34, 45, 56, 67, 78, 89]
print(n)
print(n[2:5])
print(n[:4])
print(n[4:])
print(n[-1])
print(n[-2])

#concateno liste
m = n[:2] + n[5:]
print(m)

txt = "helloworld"
print(txt[0])
print(txt[3:7])




