import re
import csv

EMAIL_RE = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

#funzione per spostare i valori da una colonna all'altra
def renameCol(row, old_name, new_name):
    val = row[old_name]
    row.pop(old_name)
    row[new_name] = val.strip()

def email_valida(email):
    if not email:
        return False
    return bool(EMAIL_RE.match(email))

def getEtaMedia(nome_file):
    eta_media = 0
    ages = []
    with open(nome_file) as fin:
        reader = csv.DictReader(fin)
        for row in reader:
            eta = row.get("Age", "").strip() #estraggo Age. se non c'è uso il default ""
            if eta.isdigit():
                ages.append(int(eta))
    eta_media = round(sum(ages) / len(ages))
    return eta_media