#creazione alias
import mymod as mod
from time import sleep
from time import sleep as pausa

#entry point
def main():
    print("eseguibile")
    mod.hello()
    sleep(1)
    pausa(1)
    mod.chisono()
    
if __name__ == "__main__":
    main()
