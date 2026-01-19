#rubrica telefonica

#struttura dati
numeri = dict()

''' funzioni disponibili
h - help
i - inserisce nuovo contatto
l - lista contatti
d - elimina un contatto
m - modifica un contatto
q - vuoi uscire s/n?
'''

#variabile che tiene attivo il ciclo
LOOP = True

while LOOP:
    ans = input("comando? (h,i,l,d,m,q): ")
    if ans == 'q':
        LOOP = False
    elif ans == 'l':
        pass
    elif ans == 'h':
        pass
    else:
        pass
        
print("bye!")
    
