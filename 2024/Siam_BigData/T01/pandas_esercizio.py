import pandas as pd

# Carica il dataset
df = pd.read_csv("sales_data.csv")

# 1. Numero totale di ordini
numero_ordini = df['InvoiceNo'].nunique()

# 2. Numero di clienti distinti
clienti_distinti = df['CustomerID'].nunique()

# 3. Valore totale delle vendite
valore_vendite_totale = df['TotalPrice'].sum()

# 4. Paese con il maggior numero di vendite
paese_max_vendite = df['Country'].value_counts().idxmax()

# 5. Data più recente e più vecchia
data_piu_recente = df['InvoiceDate'].max()
data_piu_vecchia = df['InvoiceDate'].min()

# 6. Cliente con il maggior numero di ordini
cliente_max_ordini = df['CustomerID'].value_counts().idxmax()

print("Numero totale di ordini:", numero_ordini)
print("Numero di clienti distinti:", clienti_distinti)
print("Valore totale delle vendite:", valore_vendite_totale)
print("Paese con il maggior numero di vendite:", paese_max_vendite)
print("Data più recente:", data_piu_recente)
print("Data più vecchia:", data_piu_vecchia)
print("Cliente con il maggior numero di ordini:", cliente_max_ordini)
