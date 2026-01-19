numeri = [12,23,34,45,56,67]
print(numeri)
print("primo elemento:", numeri[0])
print("secondo elemento:", numeri[1])
print("terzo elemento:", numeri[2])

print("numero di elementi: ", len(numeri))

indice = 0
print("elemento:", numeri[indice])
indice += 1
print("elemento:", numeri[indice])
indice += 1
print("elemento:", numeri[indice])

numeri[0] = 99
print(numeri)

dati = [123, "mele", 1.98, 100]
print(dati)

amici = []
cugini = list()

amici.append("Mario")
amici.append("Luigi")
amici.append("Anna")
print(amici)

amici.insert(1, "Demetrio")
print(amici)

amici.remove("Demetrio")
print(amici)

print("\n", numeri)
numeri.extend([100,200,300])
print(numeri)

numeri.pop()
print(numeri)
numeri.pop(1)
print(numeri)
numeri.remove(99)
print(numeri)

#indici negativi e slicing
print(numeri[-1])
print(numeri[2:4])
print(numeri[:4])
print(numeri[2:])

if (100 in numeri):
    print("presente")

