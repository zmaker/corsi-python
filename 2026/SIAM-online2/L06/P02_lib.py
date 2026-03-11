import os

class SimpleEditor():
    def __init__(self):
        print("Minimal PyEditor")
        self.righe = []

    def help(self):
        print("q - termina")
        print("h - help")
        print("i - inserisce una riga di testo")
        print("p - stampa il buffer")
        print("c - cancella il buffer")
        print("o - apre un file")
        print("s - salva il buffer su file")

    def insert(self):
        line = input("> ")
        self.righe.append(line)

    def prt(self):
        for i, el in enumerate(self.righe):
            print(f"{i+1} {el}")

    def clr(self):
        self.righe.clear()
        print("buffer svuotato")

    def save(self, filename):
        with open(filename, 'w') as f:
            for el in self.righe:
                f.write(el)
                f.write("\n")
            print("file salvato")

    def load(self, filename):
        if os.path.exists(filename):
            with open(filename) as f:
                for riga in f:
                    self.righe.append(riga[:-1])
                print("file caricato")
        else:
            with open(filename, 'w') as f:
                f.write("vuoto\n") 
                print("il file non esiste ne creo uno vuoto")

if __name__ == "__main__":
    print("non eseguibile")