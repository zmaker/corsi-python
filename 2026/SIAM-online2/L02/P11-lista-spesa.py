#lista della spesa

#chiedo quanti elementi servono
num_oggetti = int(input("Quante cose ti servono? "))

lista = []

for i in range(num_oggetti):
    item = input("oggetto? ")
    lista.append(item)

input("premi invio per proseguire ")

#stampo gli elementi nella lista
for i, el in enumerate(lista):
    print(f"{i+1} - {el}")