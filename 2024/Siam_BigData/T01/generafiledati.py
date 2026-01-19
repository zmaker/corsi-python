import csv
import random
from datetime import datetime, timedelta

# Funzione per generare una data casuale nel 2024
def genera_data():
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

# Apri un file CSV in modalità scrittura
with open('dati_vendite.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    # Scrivi l'intestazione
    writer.writerow(['Data', 'Importo', 'Tipo di Azione', 'Numero Conto', 'Codice Filiale'])

    # Genera 100 righe di dati
    for _ in range(100):
        data = genera_data().strftime('%Y-%m-%d')
        importo = round(random.uniform(-100, 100), 2)
        tipo_azione = random.choice(['BODA', 'DNFC', 'VERS', 'PAGO'])
        numero_conto = f'{random.randint(10, 20):05}'
        codice_filiale = random.choice(['MI001', 'MI002', 'MI003'])

        # Scrivi la riga nel file CSV
        writer.writerow([data, importo, tipo_azione, numero_conto, codice_filiale])

print("File CSV generato con successo!")
