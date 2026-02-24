class Led:
    def __init__(self, col, st="on"):
        print("init led")
        self.colore = col
        self.stato = st
        self.__tens_pn = 0.5
        
    def getColore(self):
        return self.colore

    def getStato(self):
        return self.stato
    
    def accendi(self):
        self.stato = "on"

    def spegni(self):
        self.stato = "off"

    def getTensioneGiunzione(self):
        return self.__tens_pn;
    
    def toString(self):
        return f"Led c:{self.colore} s:{self.stato} t:{self.__tens_pn}"
    
    def __str__(self):
        return f"Led c:{self.colore} s:{self.stato} t:{self.__tens_pn}"        

l1 = Led("rosso")
l2 = Led("verde")
print(l1)
print(l2)
print("col:", l1.getColore())
print("col:", l2.getColore())
print("st:", l1.getStato())
l3 = Led(col="verde", st="off")
print("col:", l3.getColore())
print("st:", l3.getStato())

print("st:", l3.stato)
print("tens pn:", l3.getTensioneGiunzione())

print(l3.toString())
l3.accendi()
print(l3.toString())
l3.spegni()
print(l3.toString())
print("-------")
print(l1)
print(l2)
print(l3)


