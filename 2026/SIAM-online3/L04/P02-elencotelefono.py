# elenco telefonico 

#elenco = dict()
elenco = {"mario":"12345", "luigi":"34567", "maria":"64678"}

while (True):
    cmd = input("comando (h per help): ")
    if (cmd == 'h'):
        print("h - help in linea")
        print("i - aggiungi contatto")
        print("p - stampa elenco contatti")
        print("q - termina il programma")
        print("s - cerca")
        print("x - elimina contatto")
        print()

    elif (cmd == 'i'):
        print("inserire nuovo contatto")
        nome = input("nome: ")
        num = input("numero telefono: ")
        elenco[nome] = num

    elif (cmd == 'p'):
        for c in elenco.items():
            nome, numero = c #unpacking ("mario":"12345463")
            print(nome, numero, sep='\t')
        print()

    elif (cmd == 's'):
        nome = input("che nome vuoi cercare? ")
        if nome in elenco:
            #se c'è, stampo il numero
            print("numero:", elenco[nome])
        else:
            print("non presente")

    elif (cmd == 'x'):
        nome = input("che nome elimini? ")
        if nome in elenco:
            elenco.pop(nome)
            print(f"eliminato {nome}")
        else:
            print("non presente")
    elif (cmd == 'q'):
        break
    else:
        print("comando non valido")