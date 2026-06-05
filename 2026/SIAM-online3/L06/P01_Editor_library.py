import os

def test():
    print("test!")

def help():
    print("editor di testi")
    print("q - termina")
    print("h - help")
    print("i - inserisce una riga di testo")
    print("p - stampa il buffer")
    print("o - apre un file")
    print("s - salva il buffer su file")
    print("c - cancella il buffer")

def getLine(righe):
    line = input("> ")
    righe.append(line)

def prt(righe):
    for i, l in enumerate(righe):
        print(i, l)
    print("") 

def readFile(filename, righe):
    righe.clear()
    if os.path.exists(filename):
        with open(filename) as f:
            for riga in f:
                righe.append(riga[:-1]) #slicing! prende tutta la riga tranne l'ultimo carattere
        print("file caricato")
    else:
        print("file non trovato")
    
def saveFile(filename, righe):
    with open(filename, "w") as f:
        for r in righe:
            f.write(r)
            f.write("\n")
    print("file salvato!")
