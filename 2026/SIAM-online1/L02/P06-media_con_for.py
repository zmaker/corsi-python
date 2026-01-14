voti = []

n_voti = int( input("quanti voti hai? ") )

for n in range(n_voti):
    n = int(input("voto: "))
    voti.append(n)

somma = 0
for el in voti:
    somma += el

print("somma voti: ", somma)

media = somma / len(voti)
print("media: ", media)
