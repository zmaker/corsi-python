def hello():
    print("hello mod")

def chisono():
    print(__name__)

def somma(a, b):
    return a + b

def main():
    print("Modulo non eseguibile")
    chisono()
    
if __name__ == "__main__":
    main()