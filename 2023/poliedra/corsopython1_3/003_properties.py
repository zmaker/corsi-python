class Led:
    def __init__(self):
        self.i = 0
        self.v = 0
        self.__tensionePN = 0.5

    def alimenta(self, i=0, v=0):
        self.i = i
        self.v = v
        
    def __str__(self):
        return f"i:{self.i} v:{self.v}"
    
    def getPN(self):
        return self.__tensionePN
    
    def setPN(self, t):
        self.__tensionePN = t
    
    
    
l1 = Led()
print(l1)
l1.i = 10
print(l1)
print(l1.i)

#print("PN:", l1._tensionePN)
print("PN:", l1.getPN())