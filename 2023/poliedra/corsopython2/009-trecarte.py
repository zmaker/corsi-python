a = int(input("A "))
b = int(input("B "))
c = int(input("C "))

if a > b:
    #confronto a e c
    if a > c:
        print("A")
    else:
        print("C")
else:
    #confronto b e c
    if b > c:
        print("B")
    else:
        print("C")
