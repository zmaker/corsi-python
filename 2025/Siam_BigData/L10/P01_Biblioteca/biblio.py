from mod_biblio import *

def main():
    #creo istanza della biblioteca
    b = Biblioteca()

    #aggiunggo libri
    b.addBook("Promessi Sposi", "Manzoni")
    b.addBook("Inferno", "Dante")
    b.addBook("Python per tutti", "M.Python")

    #stampo elenco libri
    b.printAll()

    #prendo un libro in prestito
    book = b.search("Promessi Sposi")
    print(book)


if __name__ == "__main__":
    main()