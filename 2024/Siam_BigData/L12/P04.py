import pandas as pd

ps = pd.read_csv("persone.csv", delimiter=';')
print(type(ps))
print(ps)
print(ps.dtypes)

ps['datanascita'] = pd.to_datetime(ps['datanascita'])

print(ps.dtypes)

ps['sesso2'] = ps['sesso'].apply(lambda x: 'maschio' if x == 'M' else 'femmina' )
print(ps)

ps['peso2'] = ps['peso'].apply( lambda x: 'dieta' if x >= 70 else 'ok' )
print(ps)

nomi = ps[['nome', 'cognome']]
print(nomi)

print("\nloc - etichetta (indice unico) \n--------------")
print(ps.loc[0])

print("\niloc - posizione \n--------------")
print(ps.iloc[0])

print(ps)
ps = ps.drop(1, axis=0)
print(ps)

print("nome della riga con indice 1: ", ps.index[1])
