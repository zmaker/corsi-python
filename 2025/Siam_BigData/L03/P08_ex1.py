'''
https://bit.ly/siampython2025

Programma pari e dispari - versione 2

Chiedo quanti numeri elaborare
Creo una lista vuota per i numeri pari
Creo una lista vuota per i numeri dispari

mi faccio dare i numeri, uno alla volta
    verifico se il numero è pari o dispari
    se è pari lo aggiungo alla lista dei numeri pari
    se è dispari lo aggiungo alla lista dei numeri dispari
stampo i numeri pari
stampo i nuemri dispari

'''
n = int( input("quanti numeri? ") )

pari = []
dispari = []

for i in range(n):
    numero = int( input("n: ") )
    if (numero%2) == 0:
        #pari
        pari.append(numero)
    else:
        #dispari
        dispari.append(numero)

print("pari: ")
for el in pari:
    print(el)
    
print("dispari")
for el in dispari:
    print(el)
    