from mod_biblio import *

def main(): 
    #creo istanza di biblioteca
    b = Biblioteca()

    #aggiungo i libri
    b.addBook("Promessi Sposi", "Manzoni", 123)
    b.addBook("Divina Commedia", "Dante", 124)
    b.addBook("Python per tutti", "M.Rossi", 125)

    #stampo il catalogo
    b.printAll() 

    #prendo un libro in prestito
    print()
    print("ricerca libro")
    book = b.search("Promessi Sposi")
    print(book)

    print()
    book = b.search("20000 leghe sotto ai mari")
    print(book)


if __name__ == "__main__":
    main() 