#chiedo all'utilizzatore quanti numeri vuole sommare
print("sommatore di numeri")
ans = input("quanti numeri vuoi sommare? ")
n = int(ans)

#creo una lista vuota
numeri = []

#chiedo i numeri
for i in range(n):
    ans = input(f"dammi il numero {i+1}: ")
    numero_corrente = int(ans)
    numeri.append(numero_corrente)

#print(numeri)

#presento la somma
somma = 0
for n in numeri:
    somma = somma + n
    
print(f"La somma dei numeri è: {somma}")
