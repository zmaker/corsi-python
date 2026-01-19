import pandas as pd

gruppo1 = pd.read_csv('persone.csv', delimiter=';')
gruppo2 = pd.read_csv('persone2.csv', delimiter=';')
df = pd.concat([gruppo1, gruppo2]).reset_index(drop=True)
print(df)

gr = df.groupby('sesso').groups
print(gr)

gr = df.groupby('sesso').groups['F']
print(gr)

chiave = df.groupby('sesso').groups['F'][0]
print(chiave)

for chiave, el in df.groupby('sesso'):
    print("key:", chiave)
    print(el)
    
dfm = df.groupby('sesso').get_group('M')
print(dfm)

    