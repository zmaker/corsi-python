print("for da 0 a 9")
for i in range(0, 10):
    print(i, end=" ")
    
print("\nfor con continue")
for i in range(0, 10):
    if i == 5:
        continue
    print(i, end=" ")

print("\nfor con break")
for i in range(0, 10):
    if i == 5:
        break
    print(i, end=' ')

print("\nwhile con break")
i = 0
while (i < 10):
    if i == 5:
        break
    print(i, end=' ')
    i += 1

print("\nwhile con continue")
i = 0
while (i < 10):
    i += 1
    if i == 5:
        continue
    print(i, end=' ')

