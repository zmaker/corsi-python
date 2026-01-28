import csv
import P01_MyLib as mylib

with open("dati_mailing_list.csv", newline="") as fin, \
    open("ml_output.csv", "w", newline="") as fout:

    # creo un reader per il file csv
    reader = csv.DictReader(fin)

    print("COL ORIG.:", reader.fieldnames)
    colonne = []
    for el in reader.fieldnames:
        if el == "__Email_Entered": #rinomino il campo
            el = "email"
        elif el == "First name":    #rinomino il campo
            el = "nome"
        elif el == "Surname":       #rinomino il campo
            el = "cognome"
        elif el == "Gender":       #rinomino il campo
            el = "genere"
        elif el == "Age":       #rinomino il campo
            el = "eta"
        elif el == "_CREDIT":       #rinomino il campo
            el = "credito"
        elif el == "IP_Address":    #escludo la colonna
            continue
        elif el == "Logins":        #escludo la colonna
            continue

        colonne.append(el)
    print("COL MOD.:", colonne)

    # creo il write per il file elaborato
    writer = csv.DictWriter(fout, fieldnames=colonne, extrasaction="ignore")

    #scrivo le intestazioni del file
    writer.writeheader()

    #scorro le righe del file csv
    for row in reader:
        #print(row)

        #copia campi
        mylib.renameCol(row, "First name", "nome")
        #sovrascrivo il campo e metto l'iniziale maiuscola
        row["nome"] = row["nome"].title() 

        mylib.renameCol(row, "Surname", "cognome")
        row["cognome"] = row["cognome"].title()

        mylib.renameCol(row, "__Email_Entered", "email")
        if not mylib.email_valida(row["email"]):
            #elimino la riga con email non valida
            print(row["email"], ": EMAIL KO")
            continue

        mylib.renameCol(row, "Gender", "genere")
        mylib.renameCol(row, "Age", "eta")
        
        mylib.renameCol(row, "_CREDIT", "credito")
        #trasformo il campo in float
        row["credito"] = float(row["credito"])
        if row["credito"] <= 0:
            print(row["email"], ": CREDITO <= 0")
            continue

        #scrivo la riga nel file di uscita
        writer.writerow(row)