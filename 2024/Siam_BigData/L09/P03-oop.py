class Led():
    def __init__(self, coloreled, statoled):
        print("init")
        self.colore = coloreled
        self.stato = statoled
    
    def accendi(self):
        self.stato = 1
    
    def spegni(self):
        self.stato = 0
        
    def __str__(self):
        return f"Led: {self.colore} st:{self.stato}"
    
    def __del__(self):
        print("bye bye!")

led1 = Led("verde", 1)
led1.accendi();
print(led1)
led1.spegni();
print(led1)

led2 = Led("rosso", 0)
led2.colore = "giallo"
print(led2.colore)

del led2
