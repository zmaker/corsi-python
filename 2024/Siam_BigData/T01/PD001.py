import pandas as pd
df = pd.read_csv('persone.csv', delimiter=";")
print(df)

writer = pd.ExcelWriter("pers.xlsx", engine='xlsxwriter')
df.to_excel(writer, index=False, sheet_name='Persone')
writer.close()

from sqlalchemy import create_engine
engine = create_engine('sqlite:///persdb.db')
#df.to_sql('persone', engine, index=False)

df2 = pd.read_sql("select * from persone order by cognome", engine)
print(df2)