'''
Ex.: Gioco - Indovina il numero

il computer pensa un numero tra 0 e 9
tento di indovinarlo
se indovino il numero il programma stampa u nmessaggio e il gioco finisce
se non indovino, devo riprovare
'''

import random

segreto = random.randint(0, 9)

print("Indovina il numero che ho pensato (0 - 9).")

while (True):
    num = int(input("che numero? "))
    if num == segreto:
        print("indovinato!")
        break
    else:
        print("riprova!")