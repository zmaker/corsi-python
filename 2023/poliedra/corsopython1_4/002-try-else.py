while True:
    n = 0
    try:
       n = int(input("numero: ")) 
    except ValueError:
        print("numero non valido")
    else:
        r = 100/n
        print(f"r = {r}")
    
    if n == 99:
        break