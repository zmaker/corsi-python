'''
crea un programma che chiede
due numeri all'utente e stampa:
- la somma
- la differenza
- il prodotto
- la divisione
'''
#chiedo i numeri
n = int( input("primo numero: ") )
m = int( input("secondo numero: ") )
#eseguo i calcoli e salvo i risultati in alcune variabili
s = n+m
p = n*m
d = n-m
dv = int(n/m)
#stampo
print(f"{n} + {m} = {s}")
print(n, "-", m, "=", d)
print(f"{n} x {m} = {p}")
print(f"{n} : {m} = {dv}")