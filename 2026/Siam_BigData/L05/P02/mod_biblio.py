class Biblioteca():
    def __init__(self):
        self.scaffale = []

    def addBook(self, titolo, autore, cod):
        l = Libro(titolo, autore, cod)
        self.scaffale.append(l)

    def printAll(self):
        #print(self.scaffale)
        for el in self.scaffale:
            print(el)

    def search(self, titolo):
        ans = Libro("?", "?", -1)
        for l in self.scaffale:
            if l.titolo == titolo:
                ans = l
                break
        return ans


class Libro():
    def __init__(self, titolo, autore, codice):
        self.titolo = titolo
        self.autore = autore
        self.codice = codice
        
    def __str__(self): 
        return f"[ {self.codice} ] {self.titolo} - {self.autore}"

