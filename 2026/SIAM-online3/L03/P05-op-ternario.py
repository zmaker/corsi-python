# operatore ternario

import random
n = random.randint(0,100)
print(n)

# ( codice-da-eseguire-se-true if (expr) else codice-da-eseguire-se-false )

# % è l'operatore MODULO, cioè è il resto della divisione
if ((n%2) == 0):  
    print("pari")
else:
    print("dispari")
    
print( ( "PARI" if ((n%2) == 0) else "DISPARI") )

