def sayHello():
    print("hello world")
    
sayHello()

def somma(a, b):
    s = int(a) + int(b)
    print(s)
    
somma(12, 23)

def molt(a, b):
    return a * b

m = molt(10, 2)
print(m)

def cugini(*kids):
    print(kids, "num: ", len(kids))
    print(kids[0])
    
cugini("luca", "anna")

def analizza(temp, hum, luce):
    print("temp", temp)
    print("hum", hum)
    print("luce", luce)

analizza(12, 99, 100)
analizza(hum=99, temp=12, luce=55)

def saluta(nome="Paolo"):
    print("ciao", nome)
    
saluta()
saluta("Mauro")

def multiop(a, b):
    s = a + b
    p = a * b
    return s, p

ret = multiop(10, 23)
print(ret)

n,m = multiop(10, 23)
print("s:", n, "p:", m)


