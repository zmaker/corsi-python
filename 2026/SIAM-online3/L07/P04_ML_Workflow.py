import csv
import P04_ML_Library as mylib

def main():
    with open("dati_mailing_list.csv") as fin, \
        open("ml_clean.csv", "w", newline="") as fout:
        #newline="" evita che le righe scritte nel file abbiano 2 volte il carattere di a-capo
    
        reader = csv.DictReader(fin)
        print("COLONNE ORIGINALI : ", reader.fieldnames)
        # modifico e correggo i nomi delle colonne
        # qualcuna sarà eliminata (IP e logins)
        colonne = []
        for el in reader.fieldnames:
            if el == 'First name':
                el = 'nome'
            elif el == 'Surname':
                el = 'cognome'
            elif el == '__Email_Entered':
                el = 'email'
            elif el == 'Gender':
                el = 'genere'
            elif el == 'Age':
                el = 'eta'
            elif el == '_CREDIT':
                el = 'credito'
            elif (el == 'Logins') or (el == 'IP_Address'):
                continue
            colonne.append(el)

        print("COLONNE MODIFICATE: ", colonne)

        writer = csv.DictWriter(fout, fieldnames=colonne, extrasaction="ignore")
        # extrasaction="ignore" evita che ci siano errori nel caso i nomi delle colonne non corrispondano
        # scrivo nel file i nomi dei campi
        writer.writeheader()

        for row in reader:
            print(row)

            #copia i campi
            mylib.renameCol(row, 'First name', "nome")

            val = row.pop('Surname')
            row["cognome"] = val.strip() #strip toglie gli spazi prima e dopo

            val = row.pop('__Email_Entered')
            row["email"] = val.strip()

            val = row.pop('Gender')
            row["genere"] = val.strip()

            val = row.pop('Age')
            row["eta"] = val.strip()

            val = row.pop('_CREDIT')
            row["credito"] = val.strip()
            
            writer.writerow(row)
            

if __name__ == "__main__":
    main()