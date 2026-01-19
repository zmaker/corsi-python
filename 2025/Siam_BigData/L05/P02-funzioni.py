#funzioni

def saluta():
    #corpo della funzione
    print("ciao")

def salutaConNome(nome):
    #funzione con un parametro
    print("ciao", nome)

def somma(a, b):
    #funzione con due parametri
    #che restituisce un risultato
    s = a + b
    return s
 
def elaboraNumeri(numeri):
    #funzione che riceve un parametro lista
    for el in numeri:
        print(el)

saluta()
salutaConNome("Mario")

x = somma(10,20)
print(x)

num = [1,2,3,4,5]
elaboraNumeri(num)

