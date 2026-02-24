numeri = [10, 12, 34]
nomi = ["mela", "pera", "fragola"]
prezzi = [12.1, 23.4, 34.5]

print(numeri[0])
print(numeri[1])
print(numeri)

numeri[1] = 99
print(numeri)

lista_vuota = []
print(lista_vuota)

lista_mista = [12, 23.5, "mela", 23, 12.6, "pera"]
print(lista_mista)

n = len(lista_mista)
print("elementi lista_mista: ", n)

lista_vuota.append(1)
lista_vuota.append("gatto")
lista_vuota.append(2)
lista_vuota.append("cane")
print(lista_vuota)

lista_vuota.insert(2, 999)
print(lista_vuota)

lista_vuota.extend([12, "topo"])
print(lista_vuota)

lista_vuota.remove("cane")
print(lista_vuota)

lista_vuota.pop()
print(lista_vuota)

lista_vuota.pop(2)
print(lista_vuota)

la = [1, "1", 2, "3"]
la.remove(1)
print(la)
la.remove("1")
print(la)

matrice = [[1,2,3,4], [5,6,7,8]]
print(matrice)

lb = [12,3,4,5,6,7,8,9]
print(lb[3:5])
print(lb[3:])
print(lb[:3])


