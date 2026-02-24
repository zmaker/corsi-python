while True:
    n = 0
    try:
       n = int(input("numero: "))
       assert n != 0
    except ValueError:
        print("numero non valido")
    except AssertionError:
        print("R = oo")
    else:
        r = 100/n
        print(f"r = {r}")
    
    if n == 99:
        break
