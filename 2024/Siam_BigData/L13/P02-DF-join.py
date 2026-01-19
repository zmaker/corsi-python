import pandas as pd

conti = pd.DataFrame({'conto':['0012', '0023', '0034', '0056'],
                      'intestatario':['M.Rossi','L.Bianchi','G.Verdi', 'A.Blue']})

print(conti)
saldi = pd.DataFrame({'conto':['0012', '0023', '0034'],
                      'saldo':[12300, 1000, 2500]})
print(saldi)
df = pd.merge(conti, saldi, on='conto')
print(df)
df = pd.merge(conti, saldi, on='conto', how='left')
print(df)
