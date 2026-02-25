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

    def get_temp(self):
        return self.__temp

    def set_temp(self, t):
        self.__temp = t

    temperatura = property(fget=get_temp, fset=set_temp)

    def get_i(self):
        return self.__corrente

    def set_i(self, i):
        self.__corrente = i
    
    corrente = property()
    corrente = corrente.getter(get_i)
    corrente = corrente.setter(set_i)


l1 = Led(colore="RED", stato="OFF")
l1.temperatura = 25
print(l1.temperatura)

l1.corrente = 0.1
print(l1.corrente)


