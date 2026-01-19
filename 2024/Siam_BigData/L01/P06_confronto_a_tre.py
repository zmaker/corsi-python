ans = input("A: ")
a = int(ans)

ans = input("B: ")
b = int(ans)

ans = input("C: ")
c = int(ans)

if (a > b):
    #a è maggiore di b!
    if (a > c):
        print(a)
    else:
        print(c)
else:
    #b è maggiore di a!
    if (b > c):
        print(b)
    else:
        print(c)
    