perdue = lambda x : x*2
print(perdue(10))

somma = lambda x,y : x+y
print(somma(10,20))
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
