class Led:
    
    static_var = 0
    
    def __init__(self, c="rosso", s="OFF"):
        Led.static_var += 1
        self.colore = c
        self.stato = s
    
    def __str__(self):
        return f"Led[{self.colore}]: {self.stato}"
    
    def getColor(self):
        return self.colore

    def getStato(self):
        return self.stato
    
    def getId(self):
        return Led.static_var

led1 = Led()
#print(Led.static_var)
led2 = Led(c="blu")
#print(Led.static_var)
led3 = Led(c="verde", s="ON")
#print(Led.static_var)

print(led1)
print(led2)
print(led3)


