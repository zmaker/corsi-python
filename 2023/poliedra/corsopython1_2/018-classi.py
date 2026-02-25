class Led:

    def __init__(self, col):
        print("led")
        self.colore = col
        self.stato = "OFF"
        self.__tenspn = 0.5
    
    def getColore(self):
        return self.colore
    
    def accendi(self):
        self.stato = "ON"
        
    def toString(self):
        return f"Led st:{self.stato} cl:{self.colore}"

l1 = Led("rosso")
print(l1.getColore())
print(l1.toString())
l1.accendi()
print(l1.toString())
l2 = Led("verde")
print(l1)
print(l2)

print(l1.colore)
l1.colore = "blu"
print(l1.colore)

print(l1.__tenspn)
