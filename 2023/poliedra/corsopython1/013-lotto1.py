import random

ans = 's'
while (ans == 's'):
    ans = input("estraggo un numero (s/n)?")
    #estraggo numeri a richiesta
    if ans == 's':
        n = random.randint(1,90)
        print(n, end=" ")

print("\nend")