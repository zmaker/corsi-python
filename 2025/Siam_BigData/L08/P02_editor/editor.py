from funzioni import *

#struttura dati per memorizzare il testo
testo = []

def main():
    #funzione principale in cui mettere il codice del programma
    getinfo()

    while True:
        
        cmd = input('> ')    
        if cmd == 'q':
            print("bye!")
            break
        elif cmd == 'a':
            #aggiunge linea di testo
            getLine(testo)
        elif cmd == 'p':
            #stampa testo
            printText(testo)
        elif cmd == 'h':
            #stampa menu
            getinfo()
        elif cmd == 'n':
            newBuffer(testo)
        elif cmd == 'r':
            newBuffer(testo)
            caricaTesto(testo)
        elif cmd == 's':        
            salvaTesto(testo)
        elif cmd == 'x':
            pass #codice da implementare in futuro
        elif cmd == 'd':
            eliminaRiga(testo)
        else:
            print("comando non valido")
            getinfo()
    
#test per vedere se il programma è eseguibile
if __name__ == '__main__':
    main()