import csv
import re

import mymod

EMAIL_REGEX = re.compile(
    r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
)

def email_valida(email: str) -> bool:
    if not email:
        return False
    return bool(EMAIL_REGEX.match(email))


#prima lettura per determinare l'età media
eta_media = mymod.getEtaMedia("dati_mailing_list.csv")
print("eta media", eta_media)

with open("dati_mailing_list.csv", newline="", encoding="utf-8") as fin, \
     open("output.csv", "w", newline="", encoding="utf-8") as fout:

    reader = csv.DictReader(fin)
    
    # 1. Rinomina intestazione
    fieldnames = []
    for el in reader.fieldnames:
        if el == "First name":
            el = "Nome"
        elif el == "__Email_Entered":
            el = "email"
        elif el == "_CREDIT":
            el = "credit"
             
        #ignoro una colonna
        if el == "IP_Address":
            continue
        
        fieldnames.append(el)    

    print(fieldnames)

    #inizio a scrivere l'intestazione
    writer = csv.DictWriter(fout, fieldnames=fieldnames, extrasaction="ignore")
    writer.writeheader()

    for row in reader:
        # 2. Rinomina la chiave nel dizionario riga
        val_nome = row["First name"]
        #elimino la voce
        row.pop("First name")
        #aggiungo una nuova voce
        row["Nome"] = val_nome
        
        #  __Email_Entered
        val_email = row["__Email_Entered"]
        #elimino la voce
        row.pop("__Email_Entered")
        #aggiungo una nuova voce
        row["email"] = val_email.strip()
        
        #verifico l'email e se KO non inserisco la riga
        email = row["email"]
        if not email_valida(email):
            print("scartata:", email)
            continue
        
        # se credit < 0 escludo la riga
        val_credit = float(row["_CREDIT"])
        #elimino la voce
        row.pop("_CREDIT")
        #aggiungo una nuova voce
        if val_credit > 0:
            row["credit"] = val_credit
        else:
            #salto la riga
            print("elimino", row["Nome"], "credito:", val_credit)
            continue 


        # 3. Normalizza il valore: iniziali maiuscole
        nome = row["Nome"].strip()
        row["Nome"] = nome.title()

        writer.writerow(row)