class Sensore():

    def __init__(self):
        self.__temp = 0.0
        self.__hum = 0.0

    def toF(self):
        return 32.0 + (self.__temp * 1.8)

    def getTemp(self):
        print("getter")
        return self.__temp

    def setTemp(self, t):
        print("setter")
        self.__temp = t

    def getHm(self):
        return self.__hum

    def setHm(self, h):
        if h > 100:
            h = 100.0
        elif h < 0:
            h = 0.0
        self.__hum = h

    temp = property()
    temp = temp.setter(setTemp)
    temp = temp.getter(getTemp)

    humidity = property()
    humidity = humidity.getter(getHm)
    humidity = humidity.setter(setHm)

s = Sensore()
s.temp = 23.0
print("t: ", s.temp)
s.humidity = 33.0;
print("h: ", s.humidity)


