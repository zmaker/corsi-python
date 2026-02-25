numeri = [12,23,34,45,56,7,8,3,56,4,6]

ripeti = True
while ripeti:

    n = int(input("che numero cerco? "))
    trovato = False
    for el in numeri:
        if el == n:
            trovato = True
            break

    if trovato:    
        print("trovato")
    else:
        print("non trovato")
        
    ans = input("altra ricerca (s/n)? ")
    if not (ans == 's'):
        ripeti = False
        
