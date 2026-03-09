'''
EX01 - Editor di testi
'''
import os

righe = []
filename = 'doc1.txt'

while True:
    cmd = input("cmd: ")
    if (cmd == 'q'):
        break
    elif (cmd == 'h'):
        print("q - termina")
        print("h - help")
        print("i - inserisce una riga di testo")
        print("p - stampa il buffer")
        print("c - cancella il buffer")
        print("o - apre un file")
        print("s - salva il buffer su file")
    elif (cmd == 'i'):
        line = input("> ")
        righe.append(line)
    elif (cmd == 'p'):
        for el in righe:
            print(el)
    elif (cmd == 'c'):
        righe.clear()
        print("buffer svuotato")
    elif (cmd == 's'):
        with open(filename, 'w') as f:
            for el in righe:
                f.write(el)
                f.write("\n")
            print("file salvato")
    elif (cmd == 'o'):
        righe.clear()
        if os.path.exists(filename):
            with open(filename) as f:
                for riga in f:
                    righe.append(riga[:-1])
                print("file caricato")
        else:
            with open(filename, 'w') as f:
                f.write("vuoto\n") 
                print("il file non esiste ne creo uno vuoto")
