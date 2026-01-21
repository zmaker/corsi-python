numeri = [12,23,34,12,45,56,67,12,78,89]

posizioni = []

#flag numerico
TROVATO = 0

ricerca = int( input("che numero cerco? " ))

for i, el in enumerate(numeri):
    if (ricerca == el):
        TROVATO += 1
        posizioni.append(i)

    
if TROVATO == 0:
    print("non trovato")
else:
    print(f"trovati {TROVATO} numeri")
    print(posizioni)

['mele', 'pere', 'banane']