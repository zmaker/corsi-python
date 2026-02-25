from sys import argv

def somma(a, b):
    return a + b

def diffe(a, b):
    return a - b

def molt(a, b):
    return a * b

def divi(a, b):
    if b == 0:
        return 0
    else:        
        return a / b

#entry point
def main():
    a = 0
    b = 0
    op = '+'
    
    if (len(argv) == 1):        
        a = int(input("A: "))
        b = int(input("B: "))
        op = input("op [+-:x]: ")
    else:
        a = int(argv[1])
        b = int(argv[3])
        op = argv[2]
        
    res = 0
    if op == '+':
        res = somma(a, b)
    elif op == '-':
        res = diffe(a, b)
    elif op == ':':
        res = divi(a, b)
    elif op == 'x':
        res = molt(a, b)

    print(res)

    
if __name__ == '__main__':
    if (len(argv) == 4) or (len(argv) == 1):
        main()
    else:
        print("errore parametri")
