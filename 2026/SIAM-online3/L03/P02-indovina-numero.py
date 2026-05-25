# indovina un numero

import random

segreto = random.randint(0,9)
print(segreto)

for i in range(3):
    n = int(input("che numero ho pensato? "))
    if (n == segreto):
        print("indovinato")
        break
    else:
        print("sbagliato")