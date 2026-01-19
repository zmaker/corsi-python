'''
scrivere un programma per eseguire calcoli
che chieda 2 numeri e che operazione svolgere
e quindi calcoli il risultato.

chiedo il primo numero
chiedo il secondo numero
chiedo che operazione svolggere

calcolo il risultato.
'''
print ("calcolatrice")
print("Inserire due numeri e l'operazione desiderata")
n = int(input("n1: "))
m = int(input("n2: "))

op = input("operazione (+,-,x,:): ")

#risultato del calcolo
res = 0

ERRORE = False

if (op == "+"):
    res = n + m    
elif (op == "-"):
    res = n - m
elif (op == "x"):
    res = n * m
elif (op == ":"):
    if (m == 0):
        res = 0
        #print("errore divisione per 0")
        ERRORE = True
    else:
        res = n / m
else:
    #print("?")
    op = "?"
    ERRORE = True

if (not ERRORE):
    #print("res=", res)
    print(f"{n} {op} {m} = {res}")
else:
    print("Errore: verifica i dati inseriti!")

