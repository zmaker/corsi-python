# programma per calcolare la media dei voti

voti = []

# chiedo quanti voti ci sono
num_voti = int(input("quanti voti? "))

print("chiederemo", num_voti, "voti")
#raccolgo i voti
for i in range(num_voti):
    voto = int(input("voto? "))
    voti.append(voto)

print(voti)
somma = 0
for v in voti:
    somma += v

print("somma", somma)
media = somma / num_voti
print("media", media)

