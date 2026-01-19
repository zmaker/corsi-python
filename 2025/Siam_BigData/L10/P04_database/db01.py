#creo un database sqlite3 vuoto
#importo la liberia
import sqlite3

#creo connessione al database
c = sqlite3.connect("test.db")

#chiudo la connessione
c.close()