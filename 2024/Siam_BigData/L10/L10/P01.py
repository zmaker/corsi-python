class Sensore():

    def __init__(self):
        self.temp = 0.0

    def toF(self):
        return 32.0 + (self.temp * 1.8)

s = Sensore()
s.temp = 12.0
print(s.toF())
print(s.__dict__)

