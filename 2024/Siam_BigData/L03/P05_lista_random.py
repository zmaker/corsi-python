# genera una lista di numeri casuali
import random

#creo lista vuota
numeri = []

# chiedo quanti numeri servono
ans = input("quanti numeri? ")
nmax = int(ans)

for i in range(nmax):
    #genere un numero casuale
    n = random.randint(0,99)
    #aggiungo il num alla lista
    numeri.append(n)
    
# la stampo
print(numeri)

#chiedo il numero da cercare nella lista
ans = input("Che numero? ")
num_ricerca = int(ans)

#soluzione 1
if num_ricerca in numeri:
    print("trovato!")
else:
    print("non trovato!")

#soluzione 2
for n in numeri:
    if (n == num_ricerca):
        print("trovato!")
        break

#soluzione 3
flag_trovato = False
for n in numeri:
    if (n == num_ricerca):
        flag_trovato = True
        break

if flag_trovato:
    print("Trovato (flag)")
else:
    print("NON Trovato (flag)")


