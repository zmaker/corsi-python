# lancio di un dado
import random

LOOP = True

while (LOOP):
    dado = random.randint(1,6)
    print(dado)
    
    ans = input("ancora (s/n)? ")
    if (ans != 's'):
        LOOP = False