import pandas as pd

gruppo1 = pd.read_csv('persone.csv', delimiter=';')
gruppo2 = pd.read_csv('persone2.csv', delimiter=';')
print(gruppo1)
print(gruppo2)
gfull = pd.concat([gruppo1, gruppo2]).reset_index(drop=True)
print(gfull)

stat = gfull.describe()
print(stat)
print("max:", stat['altezza'].loc['max'])