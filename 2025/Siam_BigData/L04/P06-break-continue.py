print("for da 0 a 9")

for i in range(10):
    print(i, end=' ')
    
print("\nfor con break")

for i in range(10):
    print(i, end=' ')
    if (i == 5):
        break

print("\nfor con continue")

for i in range(10):    
    if (i == 5):
        continue
    print(i, end=' ')

print("\nwhile da 1 a 10")
n = 0
while (n < 10):
    n += 1
    print(n, end=' ')

print("\nwhile con break")
n = 0
while (n < 10):
    n += 1
    if (n == 5):
        break
    print(n, end=' ')

print("\nwhile con continue")
n = 0
while (n < 10):
    n += 1
    if (n == 5):
        continue
    print(n, end=' ')
'''
cosa da non fare
print("\n")
n = 0
while (n < 10):
    print(n, end=' ')
    if (n == 5):
        continue
    n += 1
'''
    

    
    