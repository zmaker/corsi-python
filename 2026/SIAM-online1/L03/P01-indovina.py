'''
Ex: Indovina il numero

Il computer pensa un numero tra 0 e 9.
tento di indovinarlo.
se indovino il programma stampa un messaggio e termina
se non indovino, devo riprovare a dare una nuova risposta
'''
# https://docs.python.org/3/library/random.html

import random

from sqlalchemy import false

segreto = random.randint(0, 9)  # restituisce un numero casuale tra 0 e 9 (estremi inclusi)

print("Indovina il numero che ho pensato (0-9)...")

LOOP = True
while LOOP:
    #chiedo un numero al giocatore
    num = int(input("che numero? "))

    if num == segreto:
        print("Indovinato!")
        LOOP = false
    else:
        print("riprova")
