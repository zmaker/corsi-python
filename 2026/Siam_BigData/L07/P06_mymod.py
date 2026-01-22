import re
import csv

EMAIL_REGEX = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")

def email_valida(email):
    if not email:
        return False
    return bool(EMAIL_REGEX.match(email))

def renameCol(row, old_name, new_name):
    valore = row[old_name]
    row.pop(old_name)
    row[new_name] = valore

def getEtaMedia(nome_file_csv):
    media_age = 0
    ages = []
    with open(nome_file_csv, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            age = row.get("Age", "").strip()
            if age.isdigit():
                ages.append(int(age))

    media_age = sum(ages) / len(ages)
    media_age = round(media_age)

    return media_age
