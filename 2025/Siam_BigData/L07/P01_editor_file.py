# editor di testi con lettura file txt

#struttura dati per memorizzare il testo
testo = []

def getinfo():
    print("q: quit | a: add line | p: print text | h: help")
    print("n: nuovo | s: salva su file | r: legge da file")

def getLine(righe):
    linea_di_testo = input(">: ")
    righe.append(linea_di_testo)

def printText(righe):
    for r in righe:
        print(r)
        
def newBuffer(righe):
    righe.clear()

def salvaTesto(righe):
    #apro il file in scrittura
    f = open("doc1.txt", 'w') 
    #scorro righe e scrivo su file 
    for r in righe:
        #scrivo una riga dal buffer al file
        f.write(r)
        #aggiungo il carattere di "a capo"
        f.write('\n')
    
    #chiudo il file
    f.close()
    print("file salvato")

def caricaTesto(righe):
    f = open("doc1.txt")
    for l in f:
        righe.append(l[:-1])
    f.close()

getinfo()

while True:
    
    cmd = input('> ')    
    if cmd == 'q':
        print("bye!")
        break
    elif cmd == 'a':
        #aggiunge linea di testo
        getLine(testo)
    elif cmd == 'p':
        #stampa testo
        printText(testo)
    elif cmd == 'h':
        #stampa menu
        getinfo()
    elif cmd == 'n':
        newBuffer(testo)
    elif cmd == 'r':
        newBuffer(testo)
        caricaTesto(testo)
    elif cmd == 's':        
        salvaTesto(testo)
    elif cmd == 'x':
        pass #codice da implementare in futuro
    else:
        print("comando non valido")
        getinfo()

