# liste in python

numeri = [12, 23, 45, 56, 67, 78]
print(numeri)

#estraggo l'elemento alla prima posizione (cioè con indice 0)
el = numeri[0]
print("primo elemento:", el)

print(numeri[2])
#print(numeri[10])

#quanti elementi?
print("numero di elementi nella lista: ", len(numeri) )

# modifico un elemento
numeri[0] = 99
print(numeri)

# aggiungo un elemento:
numeri.append(89)
print(numeri)

#lista vuota
L1 = []
print("dim. di L1: ", len(L1))
L1.append(12)
L1.append(22)
L1.append(33)
print(L1)

# lista con tipi differenti
mag = ["mele", 120, 0.98, "pere", 78, 2.56, "kiwi", 34, 3.50]
print(mag)

# estrarre un elemento con pop()
m = [1,2,3,4,5]
print(m)
m.pop() #pop estrae l'ultimo elemento
print(m)

m.pop(0) #pop estrae l'elemento alla posizione indicata
print(m)

# remove lavora con i valori
nomi = ["max", "jim", "bob"]
print(nomi)
nomi.remove("jim")
print(nomi)

if "pamela" in nomi:
    nomi.remove("pamela")
else:
    print("pamela non trovata")
    
# slicing
#   | 0|  1|  2|  3|  4|  5|  6|  7|
n = [12, 23, 34, 45, 56, 67, 78, 89]
print("lista n:", n)
print(n[2:5])
print(n[:4])
print(n[5:])
print(n[-1])
print(n[-2])

# le stringhe sono liste
txt = "helloworld"
print(txt[0])
print(txt[3:6])






