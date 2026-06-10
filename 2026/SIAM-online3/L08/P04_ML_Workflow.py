import csv
import P04_ML_Library as mylib

def main():
    file_input = "dati_mailing_list.csv"
    file_output = "ml_clean.csv"

    with open(file_input) as fin, \
        open(file_output, "w", newline="") as fout:
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

        colonne.append("email_ok")
        print("COLONNE MODIFICATE: ", colonne)

        writer = csv.DictWriter(fout, fieldnames=colonne, extrasaction="ignore")
        # extrasaction="ignore" evita che ci siano errori nel caso i nomi delle colonne non corrispondano
        # scrivo nel file i nomi dei campi
        writer.writeheader()

        #calcolo l'eta media
        eta_media = mylib.getEtaMedia(file_input)
        print("ETA MEDIA:", eta_media)

        email_passo_precedente = ''

        for row in reader:
            #print(row)
            #copia i campi
            mylib.renameCol(row, 'First name',      "nome")
            mylib.renameCol(row, 'Surname',         'cognome')
            mylib.renameCol(row, '__Email_Entered', 'email')
            mylib.renameCol(row, 'Gender',          'genere')
            mylib.renameCol(row, 'Age',             'eta')
            mylib.renameCol(row, '_CREDIT',         'credito')
            
            #mette la prima lettera mauiuscola
            row['nome'] = row['nome'].title()
            row['cognome'] = row['cognome'].title()

            #elimino le righe con email non valida
            if not mylib.email_valida(row['email']):
                print("EMAIL KO:", row['email'])
                row["email_ok"] = 0
                #continue
            else:
                row["email_ok"] = 1

            #verifico l'eta
            val = row['eta']
            #test per individuare chi non ha inserito l'eta
            if not val.isdigit():
                print("ETA KO", row['email'])
                #inserisco il valor medio
                row['eta'] = eta_media

            #verifico il credito
            val = row['credito']
            if not val.isdigit():
                val = float(val)
                if val <= 0:
                    print("CREDITO KO:", row['email'])
                    continue
            
            #individua le righe doppie (stessa mail consecutiva)
            if (row['email'] == email_passo_precedente):
                #scarto la riga
                email_passo_precedente = row['email']
                print("MAIL DOPPIA:", row['email'])
                continue

            writer.writerow(row)

            email_passo_precedente = row['email']

            
            

if __name__ == "__main__":
    main()