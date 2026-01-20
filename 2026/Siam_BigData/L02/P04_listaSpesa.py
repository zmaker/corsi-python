'''
Esercizio
Programma per la lista della spesa

- chiedo quante cose ci sono da comperare
- metto gli oggetti in una lista
- stampo gli oggetti uno a uno
'''

noggetti = int(input("quanti oggetti? "))

spesa = []

for i in range(noggetti):
    oggetto = input(f"{i+1}: cosa ti serve? ")
    spesa.append(oggetto)

print("grazie")
input("premi INVIO per continuare")

print("\nLISTA DELLA SPESA")
for el in spesa:
    print(el)
    
conteggio = 1
for el in spesa:
    print(f"{conteggio}: {el}")
    conteggio += 1
    
for i in range(noggetti):
    print(f"{i+1}: {spesa[i]}")
    
for i, el in enumerate(spesa):
    print(f"{i+1}: {el}")
    