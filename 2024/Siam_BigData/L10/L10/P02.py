class Sensore():

    def __init__(self):
        self.__temp = 0.0

    def toF(self):
        return 32.0 + (self.__temp * 1.8)

    def getTemp(self):
        return self.__temp

    def setTemp(self, t):
        self.__temp = t

s = Sensore()
s.setTemp(12.0)
print("t: ", s.getTemp())
print(s.__dict__)

