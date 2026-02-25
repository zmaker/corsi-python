print("Cerca il numero in una lista")
numeri = [12,32,34,546,56,67,8,9,34,56,7]
print(numeri)

ripeti = True
while ripeti:
    #cerca numero    
    n = int(input("n?"))
    trovato = False

    for el in numeri:
        if n == el:
            trovato = True
            break

    if trovato:
        print("si")
    else:
        print("no")

    #gestisci loop
    ans = input("ancora (s/n)? ")
    if not (ans == 's'):
        ripeti = False
    
print("end")