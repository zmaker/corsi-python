print("for da 0 a 9")
for i in range(10):
    print(i, end = ' ')

print("\n")
print("for - con break")
for i in range(10):
    print(i, end = ' ')
    if (i == 5):
        break
    
print("\n")
print("for - con continue")
for i in range(10):    
    if (i == 5):
        continue
    print(i, end = ' ')

print("\n")
print("while - da 0 a 9")
i = 0
while (i < 10):
    print(i, end = ' ')
    i += 1

print("\n")
print("while - break")
i = 0
while (i < 10):
    if (i == 5):
        break
    print(i, end = ' ')
    i += 1
    
print("\n")
print("while - continue")
i = 0
while (i < 10):
    print(i, end = ' ')

    if (i == 5):
        i += 1
        print('X', end = ' ')
        continue
    else:
        i += 1
        
    

    