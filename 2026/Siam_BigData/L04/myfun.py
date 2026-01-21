def test():
    print("ok myfun")

def saluta():
    print("ciao")

def addio():
    print("byebye")

def sum(a, b):
    return a+b

def prod (a, b):
    return a*b

def diff(t): #t sarà una tupla con i due termini
    print(f"{t[0]} - {t[1]} = ", end='')
    return t[0] - t[1]

def div(a, b):
    if (b != 0):
        q = a / b
    else:
        q = 0
    return q

def input2():
    a = int(input("op1: "))
    b = int(input("op2: "))
    return a, b
            

def help():
    print("calcolatrice")
    print("inserire 2 numeri...")
    print("q - exit")
    print("h - help")


if __name__ == "__main__":
    print("file non eseguibile")