'''
Calcolo la media di 5 numeri usando una lista
'''

voti = []

n = int( input("voto: ") )
voti.append(n)
n = int( input("voto: ") )
voti.append(n)
n = int( input("voto: ") )
voti.append(n)
n = int( input("voto: ") )
voti.append(n)
n = int( input("voto: ") )
voti.append(n)

somma = voti[0] + voti[1] + voti[2] + voti[3] + voti[4]
print("somma: ", somma)

media = somma / len(voti)
print("media: ", media)