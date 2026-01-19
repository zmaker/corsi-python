class Sensore3():

    def __init__(self, temp = 0.0):
        self.__temp = temp
        
    def toFahrenheit(self):
        return 32 + (self.__temp * 1.8)

    def getTemp(self):
        print("get")
        return self.__temp
    
    def setTemp(self, t):
        print("set")
        if t < 0:
            t = 0;
            print("temp non permessa")
        self.__temp = t    

    #temp = property(getTemp, setTemp)
    temp = property()
    temp = temp.getter(getTemp)
    temp = temp.setter(setTemp)    


s3 = Sensore3()
s3.temp = 30.0
print(s3.temp)
s3.setTemp(-10.0)
print(s3.getTemp())
print(s3.__dict__)
