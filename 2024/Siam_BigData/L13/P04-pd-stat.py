import pandas as pd

bilancio = pd.DataFrame(index=['l','m','M','g','v','s','d'],
                        columns=['Entrate', 'Uscite'],
                        data=[[100, 75],
                              [120, 200],
                              [300, 100],
                              [490, 123],
                              [200, 456],
                              [120, 145],
                              [50, 340]])
print(bilancio)
print(bilancio.sum())
df2 = bilancio.Entrate - bilancio.Uscite
print(df2)

print((bilancio.Entrate - bilancio.Uscite).cumsum())

