#chiedo dei numeri all'utente
#e poi stampo quelli pari

#quanti numeri vuoi darmi?
ans = input("quanti numeri vuoi darmi? ")
n = int(ans)

#creo una lista vuota in cui metterò solo i numeri pari
numeri_pari = []

#ciclo for per richiedere i numeri e aggiungerli alla lista

for i in range(n):
    #chiedo il numero
    ans = input(f"dammi il numero {i+1}? ")
    num_corrente = int(ans)
    #lo aggiungo alla lista solo se è pari
    if (num_corrente%2 == 0):
        numeri_pari.append(num_corrente)
        
#stampo gli elementi con la virgola
#tranne che per l'ultimo
indice = 1
for num in numeri_pari:
    if indice < len(numeri_pari):
        print(num, end=',')
    else:
        print(num)
    indice += 1
