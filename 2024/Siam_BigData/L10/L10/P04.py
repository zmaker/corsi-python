class Sensore():

    def __init__(self):
        self.__temp = 0.0

    def toF(self):
        return 32.0 + (self.__temp * 1.8)

    @property
    def temperatura(self):
        print("get")
        return self.__temp

    @temperatura.setter
    def temperatura(self, t):
        print("set")
        self.__temp = t

s = Sensore()
s.temperatura = 17.5
print(s.temperatura)

