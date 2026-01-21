'''
calcolare la media dei voti usando una lista
1. chiedo quanti voti
2. chiedo i voti
3. faccio la media

'''

nvoti = int(input("n. voti: "))

voti = []

for i in range(nvoti):
    v = int( input(f"voto {i+1}: ") )
    voti.append(v)

somma = 0
for n in voti:
    somma += n
    #somma = somma + n

print(f"somma dei voti: {somma}")

media = somma / nvoti
print(f"media dei voti: {media}")

