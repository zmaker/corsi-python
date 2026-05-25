# programma che confronta tre numeri

a = int( input("primo numero: ") )
b = int( input("secondo numero: ") )
c = int( input("terzo numero: ") )

if (a > b):
    # a è maggiore
    if (a > c):
        print(f"{a} è il maggiore")
    elif (a < c):
        print(f"{c} è il maggiore")
    else:
        print(f"{a} = {c}, sono i maggiori")
        
else:
    #caso in cui b è maggiore
    if (b > c):
        print(f"{b} è il maggiore")
    elif (b < c):
        print(f"{c} è il maggiore")
    else:
        print(f"{b} = {c}, sono i maggiori")
        
        
        