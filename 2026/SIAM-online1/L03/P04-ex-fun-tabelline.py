# creare una funzione che stampa le tabelline
# https://docs.python.org/2/library/functions.html#range

def tabellina (num, righe=10):
    #corpo della funzione
    if (num > 0):
        #stamperemo la tabellina
        print("Tabellina del", num)
        for i in range(1, righe+1):            
            print(f"{num}x{i} = {i*num}")
    else:
        print("Solo numeri > 0")

tabellina(2, 10)
tabellina(3, 5)
tabellina(7)
tabellina(-1)

def quadrato(n):
    x = n * n
    return x

q = quadrato(10) #100
print("il quadrato di 10 è:", q)
q = quadrato(-2) #4
print("il quadrato di -2 è:", q)

