lista = [1,23,4,5,6,7,8,6,78,34,6,78,89]

ripeti = True
while ripeti:
    #ricerca numeri pari
    num_pari = 0
    for el in lista:
        n = el % 2;
        if n == 0:
            num_pari += 1
    print(f"ho trovato {num_pari} numeri pari")
    
    #gestione loop
    ans = input("ancora (s/n)? ")
    if not (ans == 's'):
        ripeti = False

print("END")