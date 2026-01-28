import re
import csv

EMAIL_REGEXP = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")

def test():
    print("ok")

def renameCol(row, old_name, new_name):
    val = row[old_name]
    row.pop(old_name)
    row[new_name] = val.strip()

def email_valida(email):
    if not email:
        return False
    return bool(EMAIL_REGEXP.match(email))

def getEtaMedia(nome_file):
    eta_media = 0
    ages = []
    with open(nome_file, newline="") as fin:
        reader = csv.DictReader(fin)
        for row in reader:
            eta = row.get("Age", "").strip()
            if eta.isdigit():
                ages.append(int(eta))

    eta_media = round(sum(ages) / len(ages))
    return eta_media