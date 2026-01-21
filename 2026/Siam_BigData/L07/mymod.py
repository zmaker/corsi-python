import csv

# ---------- PASSO 1: calcolo della media ----------
def getEtaMedia(input_file):
    ages = []

    with open(input_file, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            age = row.get("Age", "").strip() #get con default
            if age.isdigit():
                ages.append(int(age))

    if not ages:
        raise ValueError("Nessun valore valido per Age")

    media_age = sum(ages) / len(ages)

    # Arrotondamento (scegline uno)
    media_age = round(media_age)    

    return media_age