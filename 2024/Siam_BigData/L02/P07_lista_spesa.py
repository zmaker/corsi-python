#lista della spesa in Python

# PARTE 1 - chiedo cosa comprare
print("lista della spesa")

#quanti oggetti servono?
ans = input("quanti oggetti servono? ")
n = int(ans)

#creo una lista vuota
oggetti = []

#ciclo per richiedere gli elementi
for i in range(n):    
    #richiedo l'oggetto
    ans = input(f"item n.{i+1}: ")

    #aggiunggo l'oggetto alla lista
    oggetti.append(ans)

print("grazie")

# PAUSA - premi un tasto per stampare la lista
input("premi INVIO per stampare la lista")

# PARTE 2 - stampo la lista

#stampo il contenuto della lista
i = 1
for el in oggetti:
    print(f"{i}: {el}")
    i += 1

