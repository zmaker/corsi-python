# mio modulo python

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
