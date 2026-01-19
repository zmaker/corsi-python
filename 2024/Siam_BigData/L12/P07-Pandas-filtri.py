import pandas as pd

print("\nFILTRAGGIO")
ps = pd.read_csv("persone.csv", delimiter=';')
print(ps)

print("\n")
print(ps[ ps['sesso']=='M' ])

print("\n")
print(ps[ ps['peso']>=70 ])

print("\n")
# and = &
# or = |
# not = ~
print(ps[ (ps['peso']>=70) & (ps['sesso'] == 'M') ])

print("\nORDINARE")
print(ps.sort_values(by='cognome', ascending=True))

#modifica dati
ps.loc[5] = ['Maria', 'Brownz', 1.85, 78, '1995-01-01', 'F']
print(ps)
#aggiungo riga
ps.loc[10] = ['Mery', 'Brow', 1.85, 78, '1995-01-01', 'F']
print(ps)
max_chiave = ps.index.max()
print("chiave max inserita:", max_chiave)
print("chiave max inserita metodo 2:", ps.index[-1])

#cancello una riga
print(ps.drop(5, axis=0))
#cancello colonna
print(ps.drop('altezza', axis=1))

