class Led:
    def __init__(self, stato="OFF", colore="WHT"):
        print("costruttore")
        self.stato = stato
        self.colore = colore
        
    def __del__(self):
        print("distruttore")

    def __str__(self):
        return f"Led[col:{self.colore}, st:{self.stato}]"

    def accendi(self):
        self.stato = "ON"
        

l1 = Led(colore="RED", stato="OFF")
l2 = Led(colore="BLUE")
l3 = Led()
print(l1)
del l1
del l2
del l3

