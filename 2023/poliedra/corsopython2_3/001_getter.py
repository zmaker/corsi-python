class Led:
    def __init__(self, stato="OFF", colore="WHT"):
        print("costruttore")
        self.stato = stato
        self.colore = colore
        self.__tensionepn = 0.5
        
    def __del__(self):
        print("distruttore")

    def __str__(self):
        return f"Led[col:{self.colore}, st:{self.stato}]"

    def accendi(self):
        self.stato = "ON"
    
    def getTensione(self):
        return self.__tensionepn

    def setTensione(self, v):
        self.__tensionepn = v
        

l1 = Led(colore="RED", stato="OFF")
l1.colore = "GREEN"
print(l1.colore)
#print(l1.__tensionepn)
#print(l1.tensionepn
l1.setTensione(0.6)
print(l1.getTensione())

