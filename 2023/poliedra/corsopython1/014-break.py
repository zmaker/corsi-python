print("while con break")
count = 0
while count < 10:
    print(count, end=" ")
    count += 1
    if count == 5:
        break
    
print("\nwhile con continue")
count = 0
while count < 10:
    print(count, end=" ")
    count += 1
    if count == 5:
        print("X", end=" ")
        continue
    print("-", end=" ")

print("\nfor con break")
for i in range(10):
    print(i, end=" ")
    if i == 5:
        break

print("\nfor con continue")
for i in range(10):
    print(i, end=" ")
    if i == 5:
        print("X", end=" ")
        continue
    print("-", end=" ")
    
print("\nwhile con continue - errore")
count = 0
while count < 10:
    print(count, end=" ")
    if count == 5:
        print("X", end=" ")
        continue
    print("-", end=" ")
    count += 1
