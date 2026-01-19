import sys

def somma(a, b):
    return a + b

def diff(a, b):
    return a - b

def main():
    if len(sys.argv) == 4:
        #n1 = sys.argv[1]
        #op = sys.argv[2]
        #n2 = sys.argv[3]
        name, n1, op, n2 = sys.argv
        risultato = 0;
        
        n1 = int(n1)
        n2 = int(n2)
        
        if op == '+':
            risultato = somma(n1, n2)
        elif op == '-':
            risultato = diff(n1, n2)
        
        print(risultato)
        
    else:
        print("Numero parametri errato!")
        print("es: calc.py 10 + 2")

if __name__ == "__main__":
    main()    
