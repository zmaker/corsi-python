def saluta():
    #corpo della funzione
    print("ciao")

saluta()
saluta()

def salutaConNome(nome):
    #funzione con parametro
    print("ciao,", nome)

salutaConNome("mario")
n = "luigi"
salutaConNome(n)

def somma(a, b):
    s = a+b
    return s

m = 25 + somma(10, 20)
print(f"m:{m}")

z = 2
x = 3
print(somma(z, x))

def stampaPunto(x,y, colore):
    print(f"punto [{colore}] ({x},{y})")

stampaPunto(colore="blu", y=10, x=3)

def stampaPunto2(x=0,y=0, colore='nero'):
    print(f"punto [{colore}] ({x},{y})")

stampaPunto2()
stampaPunto2(colore="rosso")

def calcolatrice(n, m):
    s = n+m
    p = n*m
    return s, p

addizione, prodotto = calcolatrice(10, 20) #unpacking
print("somma:", addizione, " prod:", prodotto)

tt = calcolatrice(10, 20)
print(type(tt))

print(isinstance(tt, tuple))

