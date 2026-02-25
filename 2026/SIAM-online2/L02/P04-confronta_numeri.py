# chiedi due numeri, confrontali e scrivi qual è il maggiore

# chiedo il primo numero
n = int( input("primo numero: "))
# chiedo i secondo numero
m = int( input("secondo numero: "))

#confronto i numeri
if (n > m):
    # n è maggiore
    print(n, "è il maggiore")
elif (m > n):
    # m è maggiore
    print(m, "è il maggiore")
else:
    print("sono uguali")

