#passaggio per valore

#creo una variabile (globale)
nome = "Mario"

#creo una funzione con l'intento di farle cambiare una variabile
def cambianome(n):
    n = "Luigi"
    print("f:", n)

print("1:", nome)
cambianome(nome)
print("2", nome)

# passaggio per riferimento
num = [1,2,3,4,5]

def elabora(lista):
    lista[0] = 99
    print("f;", lista)

print("a:", num)
elabora(num)
print("b:", num)

# funzione per modificare una variabile semplcie
def cambianome2(n):
    return n.upper()

print("c:",nome)
nome = cambianome2(nome)
print("d:",nome)