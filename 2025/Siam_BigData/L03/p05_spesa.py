'''
Esercizio
Programma per la lista della spesa

- chiedo quante cose ci sono da comperare
- metto gli oggetti in una lista
- stampo gli oggetti uno a uno
'''

print("Lista della spesa")

noggetti = int(input("Quanti oggetti servono? "))

#creo una lista vuota
spesa = []

#chiedo gli oggetti da mettere nella lista
for i in range(noggetti):
    item = input(f"{i+1}. Cosa ti serve? ")
    spesa.append(item)

print("grazie.")
input("Premi INVIO per stampare la lista")

#stamp la lista della spesa
print("\nLista della spesa")
conteggio = 1 
for el in spesa:
    print(f"{conteggio}. {el}")
    conteggio += 1
    

