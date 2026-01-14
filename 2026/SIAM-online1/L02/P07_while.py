import random
import time

n = 0

while ( n != 7 ):
    #corpo del ciclo
    print(n, end=' ')
    n = random.randint(0,9)

print()
print("END")

i = 0
while (i < 10):
    print(i, end=' ')
    time.sleep(.1)
    i += 1