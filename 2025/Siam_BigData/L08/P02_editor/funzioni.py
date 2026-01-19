#funzioni per l'editor di testi

def getinfo():
    print("q: quit | a: add line | p: print text | h: help")
    print("n: nuovo | s: salva su file | r: legge da file")

def getLine(righe):
    linea_di_testo = input(">: ")
    righe.append(linea_di_testo)

def printText(righe):
    i = 1
    for r in righe:
        print(i, ":", r)
        i += 1
        
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
    
def eliminaRiga(testo):
    if len(testo) > 0:
        
        n = int(input(f"riga da eliminare (1 - {len(testo)}): "))
        #trasformo il numero di riga nell'indice
        indice = n - 1
        testo.pop(indice)
        

if __name__ == "__main__":
    print("file non eseguibile")