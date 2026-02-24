class Led:
    def __init__(self):
        self.__temp = 20
        self.__colore = "WHITE"
    
    def get_temp(self):
        return self.__temp
    
    def set_temp(self, t):
        self.__temp = t
    
    temperatura = property(fget=get_temp, fset=set_temp)

    def get_colore(self):
        return self.__colore
    
    def set_colore(self, c):
        self.__colore = c
    
    colore = property()
    colore = colore.getter(get_colore)
    colore = colore.setter(set_colore)

    
l1 = Led()
print("T: ", l1.temperatura)
l1.temperatura = 30
print("T: ", l1.temperatura)

l1.colore = "RED"
print("C: ", l1.colore)