import csv
import P06_mymod

with open("dati_mailing_list.csv", newline="") as fin, \
    open("output.csv", "w", newline="") as fout:

    reader = csv.DictReader(fin)

    #nomi delle colonne
    print("COL ORIG:", reader.fieldnames)

    #modifico i nomi delle colonne
    colonne = []
    for el in reader.fieldnames:
        if el == "First name": #modifico il nome
            el = "Nome"
        elif el == "__Email_Entered":
            el = "email"
        elif el == "_CREDIT":
            el = "credit"
        elif el == "IP_Address": #escludo la colonna 
            continue
        elif el == "Logins": #escludo la colonna 
            continue
        colonne.append(el)
    
    print("COL MOD: ", colonne)
    
    writer = csv.DictWriter(fout, fieldnames=colonne, extrasaction="ignore")
    #scrivo le intestazioni - nomi colonne
    writer.writeheader()

    #calcolo l'eta media
    eta_media = P06_mymod.getEtaMedia("dati_mailing_list.csv")
    print(eta_media)

    #creo una variabile che tiene traccia della mail della riga precendete
    prev_email = ""

    for row in reader:
        #print(row)

        P06_mymod.renameCol(row, "First name", "Nome")
        #val_nome = row["First name"]
        #row.pop("First name")
        #row["Nome"] = val_nome.strip().title()
        row["Nome"] = row["Nome"].strip().title()

        P06_mymod.renameCol(row, "__Email_Entered", "email")
        #val_email = row["__Email_Entered"]
        #row.pop("__Email_Entered")
        #row["email"] = val_email.strip()
        row["email"] = row["email"].strip()

        P06_mymod.renameCol(row, "_CREDIT", "credit")
        #escludo i clienti con credito negativo
        val_credit = float(row["credit"])
        if (val_credit <= 0):
            print(row["email"], row["credit"])
            continue
        
        #verifiche sulla email
        if not P06_mymod.email_valida(row["email"]):
            print(row["email"])
            continue
        if row["email"] == prev_email:
            print("doppia:", row["email"])
            continue

        #verifico se Age è nullo/vuoto/non numerico/mancante
        val_age = row.get("Age", "").strip()
        if not val_age.isdigit():
            row["Age"] = eta_media

        #scrivo la riga modificata
        writer.writerow(row)

        #salvo la mail per la prossima iterazione
        prev_email = row['email']

