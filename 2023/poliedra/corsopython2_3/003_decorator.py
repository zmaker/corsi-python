class Led:
    def __init__(self, stato="OFF", colore="WHT"):
        print("costruttore")
        self.stato = stato
        self.colore = colore
        self.__temp = 20
        self.__corrente = 0.0
        
    def __del__(self):
        print("distruttore")

    def __str__(self):
        return f"Led[col:{self.colore}, st:{self.stato}]"

    def accendi(self):
        self.stato = "ON"

    @property
    def temperatura(self):
        return self.__temp

    @temperatura.setter
    def temperatura(self, t):
        self.__temp = t

    @property
    def corrente(self):
        return self.__corrente
    
    @corrente.setter
    def corrente(self, i):
        self.__corrente = i
    

l1 = Led(colore="RED", stato="OFF")
l1.temperatura = 25
print(l1.temperatura)

l1.corrente = 0.1
print(l1.corrente)



