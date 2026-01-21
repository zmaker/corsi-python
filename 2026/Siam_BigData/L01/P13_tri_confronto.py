a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if (a > b):
    if (a > c):
        print("a: ", a)
    elif (a < c):
        print("c: ", c)
    else:
        print("c=a ", c)
else:
    if (b > c):
        print("b: ", b)
    elif (b < c):
        print("c: ", c)
    else:
        print("c=b ", c)