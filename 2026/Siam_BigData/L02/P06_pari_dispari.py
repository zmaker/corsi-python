'''
1. genero una lista di 10 numeri casuali
'''
import random

N = 10
numeri = []
for i in range(N):
    numeri.append(random.randint(0, 100))

print(numeri)

'''
divido la lista di numeri in due liste,
una con i numeri pari e
una con i numeri dispari
'''

pari = []
dispari = []

for el in numeri:
    if ( (el%2) == 0):
        #pari
        pari.append(el)
    else:
        #dispari
        dispari.append(el)

print(pari)
print(dispari)keep
    
    
    