def cambianome(n):
    n = "mario"
    print("f:", n)

nome = "luigi"
print("1", nome)
cambianome(nome) #passaggio per valore
print("2", nome)

def cambianome2(n):
    n = str(n).upper()
    return n

nome = cambianome2(nome)
print(nome)

# eccezione al passaggio per valore
num = [1,2,3,4,5]

def elablista(lista):
    lista[0] = 99

print("3", num)
elablista(num)
print("4", num)