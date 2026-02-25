A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))

if (A >= B):
    if (A >= C):
        print("A")
    else:
        print("C")
else:
    if (B >= C):
        print("B")
    else:
        print("C")