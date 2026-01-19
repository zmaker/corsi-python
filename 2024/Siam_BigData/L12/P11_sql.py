import pandas as pd
from sqlalchemy import create_engine

conn = create_engine('sqlite:///persone.db')
df = pd.read_sql("SELECT * FROM Persone ", conn)
print(df)

#df.iterrows()
for indice, riga in df.iterrows():
    print("indice: ", indice, riga.cognome, riga['nome'])