from sys import argv
from calclib import Calc

def main():
    parms = argv
    
    if len(parms) == 4:
        mycalc = Calc()
        mycalc.setOperando1(parms[1])
        mycalc.setOperando2(parms[3])
        mycalc.setOperatore(parms[2])
        v = mycalc.getResult()
        print(mycalc)
        
    else:
        print("parametri ko. Es: calc.py 10 x 30")

if __name__ == "__main__":
    main()