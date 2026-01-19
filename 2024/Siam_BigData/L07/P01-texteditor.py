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
    print("l - carica file")
    print("s - salva file")
    print("n - nuovo buffer")
    print("d - cancella riga")

def addrow(righe):
    row = input("> ")
    righe.append(row)

def printxt(righe):
    i = 1
    for r in righe:
        print(f"{i}: {r}")
        i += 1
        
def loadtxt(filename, righe):
    righe = []
    f = open(filename, 'r')
    lines = f.readlines()
    for ll in lines:
        righe.append(ll.replace('\n', ''))
    f.close()
    print(f"file {filename} caricato!")
    return righe

def savetxt(filename, righe):
    f = open(filename, 'w')
    for linea in righe:
        f.write(linea + '\n')
    f.close()
    print(f"file {filename} salvato!")

def newtxt():
    righe = []
    return righe;

def removeline(numero_riga):
    if (numero_riga < 0):
        print("solo da 0 in su")
    elif (numero_riga > len(righe)-1):
        print(f"al max n. {len(righe)-1}")
    else:
        righe.pop(numero_riga)
        print("eliminata riga", numero_riga)

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
    elif ans == 'l':
        ans = input("nome del file (.txt): ")
        righe = loadtxt(ans, righe)
    elif ans == 's':
        ans = input("nome del file (.txt): ")
        savetxt(ans, righe)
    elif ans == 'n':
        righe = newtxt()
    elif ans == 'd':
        ans = input("riga da eliminare: ")
        n = int(ans)
        removeline(n)
    else:
        print("comando non riconosciuto!")
        editorhelp()
        
