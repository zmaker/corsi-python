import sys
import miomodulo as m

def main():
    print("mio programma")
    m.saluta()
    
    m.saluta_nome("Luigi")
    
    print("somma: ", m.somma(12,2))

if __name__ == "__main__":
    main()    
