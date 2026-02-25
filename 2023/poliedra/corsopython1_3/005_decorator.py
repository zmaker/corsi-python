class Led:
    def __init__(self):
        self.__temp = 20
        self.__colore = "WHITE"
    
    @property
    def temperature(self):
        print("getter della temp")
        return self.__temp

    @temperature.setter
    def temperature(self, t):
        self.__temp = t
    
    
    
l1 = Led()
print("T: ", l1.temperature)
l1.temperature = 30
print("T: ", l1.temperature)

