def saluta():
    print("ciao")

def palla():
    print("boing")

saluta()
palla()

def somma(a, b):
    somma = a + b
    return somma

n = somma(10, 5)
print(n)

def elabora_numeri(lnum):
    for el in lnum:
        print(el)
        
numeri = [1,2,3,4]
elabora_numeri(numeri)

def bonifico():
    pass

print("\n---------------\nstampa persone()")
def stampa_persone(*p):
    #print(len(p))
    for nm in p:
        print(nm.upper())
    
stampa_persone("mario", "luigi", "anna")
stampa_persone("mario")

print("\n---------------\nassetto_drone()")
def assetto_drone(pitch, roll, yaw):
    print(f"assetto: p:{pitch}, r:{roll}, y:{yaw}")
    
assetto_drone(12, 3, 0)
assetto_drone(yaw=1, pitch=90, roll=23)

print("\n---------------\ndefault")
def salutanome(nome="mario"):
    print("ciao", nome)
    
salutanome("luigi")
salutanome()

print("\n---------------\nreturn2")
def calc(a, b):
    s = a+b
    p = a*b
    return s, p

n, m = calc(10, 5) #unpacking
print(f"somma: {n}")
print(f"prod: {m}")

print("\n---------------\npassaggio parametri")
def cambianome(n):
    n = "mario"
    
nome = "luigi"
print("nome prima: ", nome)
cambianome(nome)
print("nome dopo: ", nome)

def cambianome2(listanomi):
    listanomi[0] = "mario"

nomi = ["luigi"]
print("nome prima: ", nomi[0])
cambianome2(nomi)
print("nome dopo: ", nomi[0])



    




