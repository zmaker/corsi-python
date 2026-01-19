# algoritmo - trova il massimo

import random

max_val = 0

answer = 's'
while (answer == 's'):

    #estraggo un numero a caso
    n = random.randint(0,99)

    print("estratto", n)

    if (n > max_val):
        max_val = n

    print("il max fino ad ora: ", max_val)

    answer = input("ancora? (risposte possibili: s, n) ")
