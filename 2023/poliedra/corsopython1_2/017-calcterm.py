from sys import argv

def somma(a, b):
    return a + b

def prod(a, b):
    return a * b

def diff(a, b):
    return a - b

def dividi(a, b):
    if b == 0:
        return 0
    else:
        return a/b

def main():
    A = int(argv[1])
    B = int(argv[3])
    op = argv[2]
    #A = int(input("A: "))
    #B = int(input("B: "))
    #op = input("operazione: (+-/x)")
    res = 0

    if (op == '+'):
        ret = somma(A, B)
    elif (op == '-'):
        ret = diff(A, B)
    else:
        ret = 0

    print(ret)

if __name__ == "__main__":
    if len(argv) == 4:
        #print(argv, len(argv))
        main()
    else:
        print("es: 10 + 2")

