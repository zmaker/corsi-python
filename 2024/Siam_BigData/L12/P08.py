import pandas as pd

ps = pd.read_csv("persone.csv", delimiter=';')
print(ps)


writer = pd.ExcelWriter('persone.xlsx', engine='xlsxwriter')
ps.to_excel(writer, index=False, sheet_name='Pers')
writer.close()

