# creiamo una funzione che stampa le tabelline

def tabellina(num, righe=10):
    if (num >= 0):
        #
        print("Tabellina del ", num)
        for i in range(1, righe+1):
            p = num * i
            print(f"{num}x{i}={p}")
    else:
        print("solo numeri > 0")

tabellina(2)
tabellina(3, 5)
tabellina(-1)
tabellina(num=7)