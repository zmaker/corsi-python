def cambianome(n):
    n = "mario"
    print("f", n)

nome = "luigi"
print("1", nome)
cambianome(nome)
print("2", nome)

def cambianome2(n):
    n = "mario"
    print("f", n)
    return n

print("3", nome)
nome = cambianome2(nome)
print("4", nome)


num = [1,2,3,4,5,6]

def elabLista(lista):
    lista[0] = 99

print("5", num)
elabLista(num)
print("6", num)
