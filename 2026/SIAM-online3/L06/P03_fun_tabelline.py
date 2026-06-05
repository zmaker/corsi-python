# funzione che stampa le tabelline

def tabellina(base, righe=10):
    if (base > 0):
        #calcolo e stampo le tabelline
        print("Tabellina del", base)
        for i in range(1, righe+1):
            p = base * i
            print(f"{base} x {i} = {p}")

    else:
        print("Solo numeri > 0")

tabellina(2)
tabellina(3, 12)
tabellina(-1) #errore
tabellina(0) #errore
