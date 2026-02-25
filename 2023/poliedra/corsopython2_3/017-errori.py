while True:
    try:
        n = int(input("dammi un numero: "))
        assert n!= 0
    except ValueError:
        print("non è un numero valido")
    except AssertionError:
        print("oo")
    else:
        r = 100/n
        print(r);
    finally:
        print("ok");
        
    if n == 3:
        break