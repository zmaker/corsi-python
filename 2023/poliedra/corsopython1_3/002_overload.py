class Led:
    def __init__(self):
        self.i = 0
        self.v = 0

    def alimenta(self, i=0, v=0):
        self.i = i
        self.v = v
    
l1 = Led()
l1.alimenta()
print(l1.v, l1.i)
l1.alimenta(10, 5)
print(l1.v, l1.i)
l1.alimenta(i=7)
print(l1.v, l1.i)
