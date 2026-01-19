class Biblioteca():
    def __init__(self):
        self.scaffale = []
    
    def addBook(self, titolo, autore):
        #creo un oggetto libro
        l = Libro(titolo, autore)
        #aggiungo alla lista/scaffale
        self.scaffale.append(l)

    def printAll(self):
        #stampo i libri presenti 
        for l in self.scaffale:
            print(l)

    def search(self, titolo):
        ans = Libro("???", "???")
        for l in self.scaffale:
            if l.titolo == titolo:
                ans = l
                break
        return ans

class Libro():

    codice = 0

    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore
        Libro.codice += 1
        self.code = Libro.codice

    def __str__(self):
        return f"Libro ({self.code} '{self.titolo}','{self.autore}')"

if __name__ == "__main__":
    print("non eseguibile")