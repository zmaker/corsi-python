#chiedo dei numeri all'utente
#e poi stampo quelli pari

#quanti numeri vuoi darmi?
ans = input("quanti numeri vuoi darmi? ")
n = int(ans)

#creo una lista vuota
numeri = []

#ciclo for per richiedere i numeri e aggiungerli alla lista
for i in range(n):
    #chiedo il numero
    ans = input(f"dammi il numero {i+1}? ")
    num_corrente = int(ans)
    #lo aggiungo alla lista
    numeri.append(num_corrente)

#ciclo for per stampare i numeri presenti nella lista
for num in numeri:
    #il numero corrente è pari?
    if (num%2 == 0):
        #se è pari lo stampo
        print(num, end=',')
