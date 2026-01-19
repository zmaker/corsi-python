import sys
from modulocalc import somma
from modulocalc import diff

def main():
    if len(sys.argv) == 4:
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
