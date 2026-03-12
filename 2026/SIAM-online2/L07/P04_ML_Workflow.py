import csv
import P04_ML_lib as mylib

def main():
    with open("dati_mailing_list.csv") as fin, \
        open("ml_clean.csv", "w", newline="") as fout:

        reader = csv.DictReader(fin)
        print("COL ORIG:", reader.fieldnames)

        #modifico e correggo i nomi delle colonne
        #alcune saranno eliminate
        colonne = []
        for el in reader.fieldnames:
            if el == "__Email_Entered": #rinomino
                el = "email"
            elif el == "First name":
                el = "nome"
            elif el == "Surname":
                el = "cognome"
            elif el == "Gender":
                el = "genere"
            elif el == "Age":
                el = "eta"
            elif el == "_CREDIT":
                el = "credito"
            elif el == "IP_Address": #elimino colonna
                continue
            elif el == "Logins":
                continue

            colonne.append(el)
        print("COL MOD:", colonne)

        writer = csv.DictWriter(fout, fieldnames=colonne, extrasaction="ignore")
        #scrivo le intestazioni del file
        writer.writeheader()

        #calcolo l'eta media
        eta_media = mylib.getEtaMedia("dati_mailing_list.csv")

        for row in reader:
            #print(row)

            #copia i campi
            mylib.renameCol(row, "First name", "nome")
            row['nome'] = row['nome'].title()
            
            mylib.renameCol(row, "Surname", "cognome")
            row['cognome'] = row['cognome'].title()
            
            mylib.renameCol(row, "__Email_Entered", "email")
            if not mylib.email_valida(row['email']):
                #la mail non è valida -> elimino la riga
                print(row['email'], "EMAIL NON VALIDA")
                continue
            
            mylib.renameCol(row, "Gender", "genere")

            mylib.renameCol(row, "Age", "eta")
            val = row["eta"]
            if not val.isdigit():
                print(row['email'], "ETA MANCANTE", eta_media)
                row['eta'] = eta_media

            mylib.renameCol(row, "_CREDIT", "credito")
            row['credito'] = float(row['credito'])
            if row["credito"] <= 0:
                print(row['email'], "CREDITO <= 0", row["credito"])
                continue

            writer.writerow(row)
            #break


if __name__ == "__main__":
    main()