import pandas as pd

df = pd.DataFrame()
print(df)

df2 = pd.DataFrame(['Milano', 'Roma', 'Napoli', 'Palermo'])
print(df2)

df3 = pd.DataFrame(columns=['citta','regione','abitanti'],
                   data=[['Milano','Lom', 234560],
                         ['Roma', 'Laz', 1234567],
                         ['Palermo','Sic', 345678]])
print(df3)

print("\nDF con Series ------------")
capitali = pd.Series(index=['ITA','FRA','DEU', 'GRE'],
                     data= ['Roma', 'Parigi', 'Berlino', 'Atene'])
popolazione = pd.Series(index=['ITA', 'FRA', 'DEU'],
                        data= [123400, 234500, 456700])
df4 = pd.DataFrame({'capitali':capitali, 'popolazione':popolazione})
print(df4)

