import random

numeri = []

maxnum = int( input("quanti numeri? ") )
tipo = int( input("(1)pari o (2)dispari? ") ) 

for n in range(maxnum):
    x = random.randint(0,100)
    numeri.append(x)

print("numeri: ", numeri)

for n in numeri:
    if ((n%2) == (0 if tipo == 1 else 1)):
        print(n, end=' ')
        
        