import pandas as pd

ps = pd.read_csv("persone.csv", delimiter=';')
#seleziono usando la chiave della riga
print(ps.loc[1:3])
#seleziono usando l'indice della riga
print(ps.iloc[1:3])

print("\nsubset\n--------")
print(ps.iloc[1:3]['cognome'])

print("\nsubset con più colonne\n------------------")
print(ps.iloc[1:3][['cognome', 'altezza']])

print("\nprime righe di un datafile\n------------------")
print(ps.head(2))

print("\nultime righe di un datafile\n------------------")
print(ps.tail(2))

print("\nSeries\n----------------------")
cognomi = ps['cognome']
print(cognomi)
print(type(cognomi))

#creazione di una Series
citta = pd.Series(data=['Milano', 'Roma', 'Napoli', 'Palermo'])
print(citta)
print(type(citta))
#numpy
import numpy as np
arraynumpy = np.array([12,23,34,45,56,67,78])
nf = pd.Series(data=arraynumpy)
print(nf)
print(type(nf))
#dict

capitali = {'Italia':'Roma', 'Francia':'Parigi', 'Grecia':'Atene'}
nf = pd.Series(capitali)
print(nf)
print(type(nf))


