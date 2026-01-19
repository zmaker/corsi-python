'''
Text editor in Python

- riceve una riga di testo per volta
- memorizza le righe di testo in una lista

- visualizzo il testo

- posso eliminare una riga di testo

extra
- inserisco una riga di testo in una posizione a piacere

'''

righe = []

def editorhelp():
    print("h - help")
    print("i - inserisce una linea")
    print("c - cancella il buffer")
    print("p - stampa il buffer")
    print("q - esci")
    
def insertline():
    linea = input(">")
    righe.append(linea)
    
def printtext():
    for l in righe:
        print(l)
        
def cleartext():
    righe.clear()

editorhelp()
while (True):
    cmd = input("comando? ") 
    if not cmd:
        break;
    elif (cmd == 'h'):
        #visualizza l'help
        editorhelp()
    elif (cmd == 'i'):
        #inserire una linea
        insertline()
    elif (cmd == 'p'):
        #stampa il testo completo
        printtext()
    elif (cmd == 'c'):
        #svuota il testo
        cleartext()
    elif (cmd == 'q'):
        #termina il programma
        break
    else:
        print("?")