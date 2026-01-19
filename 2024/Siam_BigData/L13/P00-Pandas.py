# ripasso di pandas
import pandas as pd

#import da csv
df = pd.read_csv('persone.csv', delimiter=';')
print(df)

df2 = df[['altezza', 'peso']]
print(df2.loc[0:2])
print(df2.iloc[0])

#filtraggi
df3 = df[ df['sesso'] == 'M' ]
print(df3)

#order
df4 = df.sort_values(by='peso', ascending=True)
print(df4)
print(df4.loc[0])
print(df4.iloc[0])

df4.to_csv('elab.csv', index=None, sep=';', header=True)

## per excel: XlsxWriter
#salvo in excel
wri = pd.ExcelWriter('elab.xlsx', engine='xlsxwriter')
df4.to_excel(wri, index=False, sheet_name='Persone')
wri.close()

#carico excel
dfx = pd.read_excel('elab.xlsx')
print(dfx)

# sqlalchemy
from sqlalchemy import create_engine
conn = create_engine('sqlite:///database.db')
df.to_sql('persone', conn, index=True)





