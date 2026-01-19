'''
Ex: Indovina il numero

Il computer pensa un numero tra 0 e 9.
tento di indovinarlo.
se indovino il programma stampa un messaggio e termina
se non indovino, devo riprovare a dare una nuova risposta
'''
#https://docs.python.org/3/library/random.html
import random

print("Indovina il numero")
print("Ho pensato a un numero. Sai indovinarlo?")

segreto = random.randint(1, 90)
print(segreto)

LOOP = True
while (LOOP):
    #chiedo un numero al giocatore
    num = int( input("che numero: ") )
    if (num == segreto):
        print("Indovinato!")
        LOOP = False
    else:
        print("Ritenta...")
