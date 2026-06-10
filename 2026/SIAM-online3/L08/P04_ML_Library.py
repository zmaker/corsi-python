import re
import csv

#Preparo la Regular Expression (RegExpr)
EMAIL_RE = re.compile(r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$")

def renameCol(row, old_name, new_name):
    val = row.pop(old_name)
    row[new_name] = val.strip()

def email_valida(email):
    if not email: #se email è vuota
        return False
    return EMAIL_RE.match(email)

def getEtaMedia(filename):
    eta_media = 0
    ages = []
    with open(filename) as fin:        
        reader = csv.DictReader(fin)
        for row in reader:
            eta = row.get("Age", "").strip() #get restituisce il valore con un default ""
            if eta.isdigit():
                ages.append(int(eta))
    eta_media = int(sum(ages)/len(ages))
    return eta_media

if __name__ == '__main__':
    print("File non eseguibile")