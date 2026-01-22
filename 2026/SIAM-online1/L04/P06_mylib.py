# mio modulo python

import os

def test():
    print("TEST OK")

def saluta():
    print("hello")

def editorhelp():
    print("PyEditor")
    print("h - help")
    print("i - inserisci riga di testo")
    print("c - cancella il buffer")
    print("p - stampa buffer")
    print("o - open file")
    print("s - save file")
    print("q - esci")
    print()

def insertline(lista):
    line = input("> ")
    lista.append(line)

def printbuffer(lista):
    for el in lista:
        print(el)
        
def clearbuffer(lista):
    lista.clear()
    print("ok")

def openFile(lista):
    lista.clear()
    nomefile = "doc1.txt"
    if os.path.exists(nomefile):
        with open(nomefile) as f:
            for riga in f:
                lista.append(riga[:-1])
        print("file caricato")
        printbuffer(lista)
    else:
        with open("doc1.txt", "w") as f:    
            f.write("empty\n")

def saveFile(lista):
    with open("doc1.txt", "w") as f:
        for riga in lista:
            f.write(riga)
            f.write("\n")
    print("file salvato")