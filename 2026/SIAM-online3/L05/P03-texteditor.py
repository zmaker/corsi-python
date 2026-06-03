import os

righe = []
filename = "doc1.txt"

while True:
    cmd = input("cmd: ")
    if (cmd == 'q'):
        break
    elif (cmd == 'h'):
        print("editor di testi")
        print("q - termina")
        print("h - help")
        print("i - inserisce una riga di testo")
        print("p - stampa il buffer")
        print("o - apre un file")
        print("s - salva il buffer su file")
        print("c - cancella il buffer")

    elif (cmd == 'i'):
        line = input("> ")
        righe.append(line)

    elif (cmd == 'p'):
        for i, l in enumerate(righe):
            print(i, l)
        print("")   

    elif (cmd == 'o'):
        righe.clear()
        if os.path.exists(filename):
            with open(filename) as f:
                for riga in f:
                    righe.append(riga[:-1]) #slicing! prende tutta la riga tranne l'ultimo carattere
            print("file caricato")
        else:
            print("file non trovato")

    elif (cmd == 's'):
        with open(filename, "w") as f:
            for r in righe:
                f.write(r)
                f.write("\n")
        print("file salvato!")

    elif (cmd == 'c'):
        righe.clear()
        print("buffer svuotato")

    else:
        print("???")    