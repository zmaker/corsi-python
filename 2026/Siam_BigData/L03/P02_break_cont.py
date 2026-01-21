#ciclo for - 0-9
for i in range(0,10):
    print(i, end=' ')

print("") #va a capo dopo l'ultimo valore

#ciclo for - 0-9
for i in range(0,10):
    print(i, end=' ')
    if (i == 5):
        break

print("") #va a capo dopo l'ultimo valore

#ciclo for - 0-9
for i in range(0,10):
    if (i == 5):
        continue
    print(i, end=' ')

print("") #va a capo dopo l'ultimo valore


#while da 0 a 9
print("while")
count = 0
while count < 10:
    print(count, end=' ')
    count += 1
    
print("\nwhile - break")
count = 0
while count < 10:
    print(count, end=' ')
    if (count == 5):
        break
    count += 1

print("\nwhile - continue")
count = 0
while count < 10:
    count += 1
    if (count == 5):
        continue
    print(count, end=' ')
    



