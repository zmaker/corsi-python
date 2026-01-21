# calcolatrice - con file eseguibile
import myfun
from myfun import saluta
from myfun import addio as bye

def main():
    #myfun.test()
    #saluta()
    #bye()
    RUN = True
    while (RUN):
        cmd = input("?")
        if (cmd == 'q'):
            RUN = False
        elif (cmd == '+'):
            #a = int(input("op1: "))
            #b = int(input("op2: "))
            a, b = myfun.input2()
            s = myfun.sum(a, b)
            print(f"{a} + {b} = {s}")
            
        elif (cmd == '*'):
            #a = int(input("op1: "))
            #b = int(input("op2: "))
            a, b = myfun.input2()
            s = myfun.prod(a, b)
            print(f"{a} * {b} = {s}")

        elif (cmd == '-'):
            s = myfun.diff(myfun.input2())
            print(s)
        elif (cmd == ':'):
            pass
        elif (cmd == 'h'):
            myfun.help()
        else:
            myfun.help()


if __name__ == "__main__":
    main()
