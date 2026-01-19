'''
Text editor in Python

- riceve una riga di testo per volta
- memorizza le righe di testo in una lista

- salvo la lista di righe in un file di testo
- posso dare il nome che voglio al file da salvare

- carica un file di testo dandogli il nome

- visualizzo il contenuto del file

- posso eliminare una riga di testo

extra
- inserisco una riga di testo in una posizione a piacere

'''
righe = []

def editorhelp():
    print("i - inserisci una riga di testo")
    print("h - help")
    print("p - stampa contenuto")

def addrow(righe):
    row = input("> ")
    righe.append(row)

def printxt(righe):
    for r in righe:
        print(r)

while (True):
    ans = input("cmd (h=help)? ")
    if not ans:
        break
    elif ans == 'h':
        editorhelp()
    elif ans == 'i':
        addrow(righe)
    elif ans == 'p':
        printxt(righe)
        
