'''
Rubrica telefonica
'''
print("Rubrica Telefonica V1")
elenco = dict()

while (True):
    cmd = input("comando (q,h,l,i,s,d): ")
    if (cmd == 'q'):
        break
    elif (cmd == 'h'):
        print("q per finire")
        print("h per l'help")
        print("l lista numeri")
        print("i inserisci numero")
        print("s cerca numero")
        print("d elimina numero")
        
    elif (cmd == 'l'):
        for el in elenco.items():
            nome, num = el #unpacking 
            print(f"{nome}: {num}")

    elif (cmd == 'i'):
        nome = input("nome: ")
        numero = input("numero: ")
        elenco[nome] = numero

    elif (cmd == 's'):
        nome = input("nome da cercare: ")
        if nome in elenco:
            tel = elenco[nome]
            print(f"n.: {tel}")
        else:
            print("non presente") 

    elif (cmd == 'd'):
        nome = input("nome da eliminare: ")
        if nome in elenco:
            elenco.pop(nome)
        else:
            print("non presente")


print("grazie per aver usato il programma")