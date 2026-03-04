import random

# creo una lista vuota da riempire con dei numeri casuali
numeri = []

# inserisco 10 numeri
for i in range(0, 10):
    numeri.append( random.randint(0, 99) )
    
for n in numeri:
    d = n % 2 #% modulo: il resto della divisione
    if (d == 0):
        print(n, end=", ")


