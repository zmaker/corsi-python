numeri = [2, 3, 4, 5, 6, 8, 10, 23, 34, 45, 56]

for n in numeri:
    d = n % 2 #% modulo: il resto della divisione
    if (d == 0):
        print(n, end=", ")