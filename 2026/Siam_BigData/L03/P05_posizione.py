numeri = [12,23,34,12,45,56,67,12,78,89]

posizioni = []

#flag numerico
TROVATO = 0

ricerca = int( input("che numero cerco? " ))

i = 0
for el in numeri:
    if (ricerca == el):
        TROVATO += 1
        posizioni.append(i)
    i += 1
    
if TROVATO == 0:
    print("non trovato")
else:
    print(f"trovati {TROVATO} numeri")
    print(posizioni)
