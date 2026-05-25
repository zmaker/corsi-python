# lancio di un dado
import random

while (True):
    dado = random.randint(1,6)
    print(dado)
    
    ans = input("ancora (s/n)? ")
    if (ans != 's'):
        break
