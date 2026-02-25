def f1():
    a = 20
    print("a in f1 vale: ", a)

a = 10
print(a)
f1()
print(a)

def f2():
    global a
    a = 20
    print("a in f1 vale: ", a)

a = 10
print(a)
f2()
print(a)



