import pandas as pd
from sqlalchemy import create_engine

ps = pd.read_csv("persone.csv", delimiter=';')
print(ps)

conn = create_engine('sqlite:///persone.db')
ps.to_sql('persone', conn, index=False)
