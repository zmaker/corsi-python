'''
Programma pari e dispari

Chiedo quanti numeri elaborare
Creo una lista vuota per i numeri pari
mi faccio dare i numeri, uno alla volta
    verifico se il numero è pari o dispari
    se è pari lo agggiungo a una lista
stampo i numeri pari

Come capisco se un numero è pari o dispari?
Uso l'operatore modulo %
10 % 2 = 0
11 % 2 = 1
2  % 2 = 0
3  % 2 = 1

Se il risultato di modulo è 0 allora il numero è pari
altrimenti è dispari.
'''
print("Seleziono solo numeri pari")
num = int( input("Quanti numeri mi darai? ") )

#creo una lista vuota per memorizzare i numeri pari
num_pari = []

# ripeto per num volte
for i in range(num):
    n = int( input("che numero? ") )
    if ((n%2) == 0):
        #il numero è pari
        #lo aggiungo alla lista
        num_pari.append(n)
        
#stampo tutti i numeri pari ricevuti
print("i numeri pari sono:")
for n in num_pari:
    print(n, end=" ")


