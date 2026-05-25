import random

n = random.randint(0, 10)
# ripeto fino a che non trovo 7
while not (n == 7): # diverso da: !=
    print(n, end=' ')
    n = random.randint(0, 10)
    
print()

#conteggio da 0 a 9
i = 0
while (i < 10):
    print (i, end=' ')
    i += 1 #aumento i di 1 unita

print()

# while con una lista
numeri = [1,23,34,45,56,67,78,88]

i = 0
while (i < len(numeri)):
    print(i, numeri[i])
    i += 1
