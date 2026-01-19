print("Confronto tre numeri")

a = int( input("primo numero: ") )
b = int( input("secondo numero: ") )
c = int( input("terzo numero: ") )

if (a > b):
    #A è maggiore di B: tengo A e butto B
    #qui confronto A e C
    if (a > c):
        #vince A
        print("a", a)
    else:
        #vince C
        print("c", c)
    
else:
    #B è maggiore di A: tengo B e butto A
    #qui confronto B e C
    if (b > c):
        #vince B
        print("b", b)
    else:
        #vince C
        print("c", c)
    