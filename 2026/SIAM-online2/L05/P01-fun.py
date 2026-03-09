# funzioni in python

#prima funzione - senza parametri
def saluta():
    #corpo della funzione
    # funziona che saluta
    print("ciao!")

saluta()
saluta()

#funzione con un parametro
def salutaConNome(nome):
    print("ciao,", nome)

salutaConNome("luigi")

#funzione che restituisce un risultato
def somma(a, b):
    s = a + b
    return s

n = somma(10, 20)
print(n)
print(somma(12, 23))
p = 23
q = 45
print(somma(p, q))

#parametri nominali
def stampaPunto(x, y, colore):
    print(f"punto: ({x},{y}) di colore {colore}")

stampaPunto(10,20,"red")
stampaPunto(y=23, colore='blue', x=2)

#valori di default
def stampaLinea(xi=0, yi=0, xf=10, yf=10, colore='nero'):
    print(f"linea: ({xi},{yi})-({xf},{yf}) di colore {colore}")

stampaLinea()
stampaLinea(xi=0, yi=10, xf=100, yf=120)
stampaLinea(xf=100, yf=120, xi=0, yi=10)

#restituire valori multipli
def calc(a, b):
    s = a+b
    p = a*b
    return s, p #packing

x = calc(10, 20)
print(x, type(x))
print(isinstance(x, tuple))

s1, p1 = calc(23, 34) #unpacking
print("somma: ", s1, " prodotto: ", p1)
