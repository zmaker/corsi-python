# programma interattivo

# genera lista di numeri casuali
import random

#creo lista vuota
numeri = []

# chiedo quanti numeri servono
ans = input("quanti numeri? ")
nmax = int(ans)

for i in range(nmax):
    #genere un numero casuale
    n = random.randint(0,99)
    #aggiungo il num alla lista
    numeri.append(n)

# chiede se si vuole cercare un numero (s/n)
ans = 's'
while (ans == 's'):
    #chiedo il numero da cercare nella lista
    ans = input("Che numero? ")
    num_ricerca = int(ans)

    # esegue l'operazione
    if num_ricerca in numeri:
        print("trovato!")
    else:
        print("non trovato!")
    
    #eseguo di nuovo?
    ans = input("Altra ricerca? (s/n) ")

# termina il programma
print("Grazie per aver usato il programma")
