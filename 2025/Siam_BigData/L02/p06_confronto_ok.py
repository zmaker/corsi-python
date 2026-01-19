print("Confronto due numeri")
n = int( input("primo numero: ") )
m = int( input("secondo numero: ") )

if (n > m):
    print(f"{n} > {m}: primo numero è il maggiore")
    
elif (n < m):
    print(f"{m}: secondo numero è il maggiore")
    
else:
    print(f"{m} e {n} sono uguali")


