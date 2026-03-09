# modulo con funzioni per l'editor di testi
import os

def test():
    print("test")

def help():
    print("q - termina")
    print("h - help")
    print("i - inserisce una riga di testo")
    print("p - stampa il buffer")
    print("c - cancella il buffer")
    print("o - apre un file")
    print("s - salva il buffer su file")

def insert(righe):
    line = input("> ")
    righe.append(line)

def prt(righe):
    for i, el in enumerate(righe):
        print(f"{i+1} {el}")

def clr(righe):
    righe.clear()
    print("buffer svuotato")

def save(filename, righe):
    with open(filename, 'w') as f:
        for el in righe:
            f.write(el)
            f.write("\n")
        print("file salvato")

def load(filename, righe):
    if os.path.exists(filename):
        with open(filename) as f:
            for riga in f:
                righe.append(riga[:-1])
            print("file caricato")
    else:
        with open(filename, 'w') as f:
            f.write("vuoto\n") 
            print("il file non esiste ne creo uno vuoto")