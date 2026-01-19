import pandas as pd
import matplotlib.pyplot as pl

df = pd.read_csv('azioni.csv', delimiter=';')
print(df)

df['chiusura'].plot(kind='line')
df['chiusura'].rolling(window=3).mean().plot(kind='line')
pl.show()