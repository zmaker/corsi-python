print("sei in una foresta magica e il sole sta tramontando.")
print("Da che parte vai?")
move = input("N, S, W, E, U? ")

match move:
    case 'N' | 'U':
        print("sei uscito dalla foresta")
    case 'S':
        print("la foresta è ancora più folta")
    case 'W':
        print("tra gli alberi appare una capanna")
    case 'E':
        print("dalla radura spunta un wumpus affamato")
    case _:
        print("comando non valido")