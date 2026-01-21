numeri = [12,23,34,45,56,67,78,89]

n = int(input("che numero cerco? "))

TROVATO = False

for el in numeri:
    if (n == el):
        TROVATO = True
        break
    
if TROVATO:
    print("trovato")
else:
    print("non trovato")