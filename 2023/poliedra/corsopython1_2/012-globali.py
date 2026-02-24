a = 10

def f1():
    a = 20
    print("f1 says: ", a)
    
print(a)
f1()
print("dopo f1", a)

def f2():
    global a
    a = 20
    print("f1 says: ", a)

print(a)
f2()
print("dopo f2", a)
