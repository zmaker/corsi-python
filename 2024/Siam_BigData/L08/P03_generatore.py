def sequenza(x):
    while(True):
        yield x
        x += 1

i = sequenza(10)
print(next(i))
print(next(i))
print(next(i))

g = sequenza(0)
for i in g:
    print(i)
    if (i == 10):
        break