n = 0
try:
    n = int(input("numero: "))
except ValueError:
    print("num non valido")
else:    
    if n != 0:
        r = 100/n
        print("R: ", r)
    else:
        print("R: infinito")

