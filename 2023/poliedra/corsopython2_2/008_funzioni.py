def saluta():
    print("hello")
    
saluta()

def somma(a, b):
    c = a + b
    print("s:", c)
    
somma(10, 20)

def molt(a, b):
    return a * b

n = 10
m = 20
x = molt(n, m)
print(x)

def cugini(*cug):
    print(cug, len(cug))
    for el in cug:
        print("cugino: ", el)
    print("primo cug:", cug[0])
    
cugini("mario", "anna", "daniele")

def controllo(temp, hum, luce):
    print("controllo (",temp, hum, luce, ")" )
    
controllo(24, 99, 67)
controllo(luce=100, hum=45, temp=12)

def controllo2(temp=10, hum=0, luce=0):
    print("controllo (",temp, hum, luce, ")" )

controllo2(temp=23)

def multiop(a, b):
    s = a + b
    p = a * b
    d = a - b
    return s, p, d

ret = multiop(12, 34)
print(ret)

a, b, c = multiop(12, 34)
print("a:", a)
print("b:", b)
print("c:", c)


    
