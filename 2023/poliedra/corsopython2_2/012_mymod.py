import modulo
#import time
from time import sleep
from time import sleep as pausa
import os as sysop

#entry point
def main():
    print("main")
    modulo.saluta()
    print(modulo.somma(10, 23))
    #time.sleep(1)
    sleep(1)
    pausa(1)
    modulo.chisono()
    
if __name__ == '__main__':
    main()
