'''
Ex: Indovina il numero
'''
#https://docs.python.org/3/library/random.html
import random

print("Indovina il numero")
print("Ho pensato a un numero. Sai indovinarlo?")

segreto = random.randint(1, 90)
print(segreto)

tentativi = 0

LOOP = True
while (LOOP):
    #chiedo un numero al giocatore
    num = int( input("che numero: ") )
    
    #print("t: ", tentativi)
    if (num == segreto):
        print("Indovinato!")
        LOOP = False
    else:        
        tentativi += 1
        if (tentativi >= 3):
            print("Troppi tentativi")
            LOOP = False;
        else:
            print("Ritenta...")    

