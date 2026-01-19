
def cambianome(n):
    n = "mario"
    print("f", n)

def cambianome2(n):
    n = "mario"
    print("f", n)
    return n


nome = "luigi"

print("1", nome)
cambianome(nome)
print("2", nome)

print("3", nome)
nome = cambianome2(nome)
print("4", nome)
