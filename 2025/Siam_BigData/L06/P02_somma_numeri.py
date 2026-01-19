# esercizio
# data la stringa:
dati = "23,  45 ,55,  65, 89, 37, 100, 33, 77   "

#calcolate la media dei numeri

lista = dati.split(',')
lista_pulita = []
for n in lista:
    #tolgo gli spazi in eccesso
    num = n.strip()
    #trasformo in numero
    num = int(num)
    #salvo il num nella nuova lista
    lista_pulita.append(num)

print(lista_pulita)

somma = 0
for n in lista_pulita:
    somma = somma + n

print("somma:", somma)
#quanti numeri nella lista?
n_elementi = len(lista_pulita)
media = somma / n_elementi

print("media:", media)