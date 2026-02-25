from calclib import Calc
from sys import argv

def main():
    parms = argv
    
    if not len(parms) == 4:
        print("Parametri non corretti! usa: calc 10 + 20")
    else:
        mycalc = Calc()
        mycalc.setOperando1(parms[1])
        mycalc.setOperando2(parms[3])
        mycalc.setOperazione(parms[2])
        res = mycalc.getResult()
        print(mycalc)

if __name__ == "__main__":
    main()