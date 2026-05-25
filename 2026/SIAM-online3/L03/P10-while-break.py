import time

i = 0
while (i < 10):
    print(i, end=' ')
    i += 1
    
print()

i = 0
while (i < 10):
    print(i, end=' ')
    if (i == 4):
        break
    i += 1

print()

i = 0
while (i < 10):
    i += 1    
    if (i == 4):
        continue
    print(i, end=' ')
    time.sleep(1)
