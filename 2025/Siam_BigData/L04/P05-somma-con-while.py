#codice per ripetere un programma

LOOP = True

while (LOOP):
    #corpo
    
    a = int( input("A: ") )
    b = int( input("B: ") )
    print(f"{a} + {b} = {(a+b)}")
    
    ans = input("ancora (s/n)?: ")
    if ans != 's':
        LOOP = False
        
