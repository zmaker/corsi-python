'''
Calcolo la media di 5 numeri usando una lista
'''

voti = []

for i in range(5):
    print(f"{i+1}) - ", end=' ') 
    voto = int( input("voto: ") )
    voti.append(voto)

somma = 0
for n in voti:
    #print(n)
    somma = somma + n;
    #ioppure si può usare la forma compatta
    #somma += n

print("somma: ", somma)

media = somma / len(voti)
print("media: ", media)