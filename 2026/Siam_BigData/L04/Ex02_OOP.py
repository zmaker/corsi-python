#OOP in python

class Led:
    pass

l1 = Led()
print(l1)
l2 = Led()
print(l2)

class Led2:
    def __init__(self):
        print("creato led!")

l3 = Led2()

class Led3:
    def __init__(self, col, st):
        self.colore = col
        self.stato = st

    def __str__(self):
        return f"Led {self.colore} - st:{self.stato}"

    def accendi(self):
        self.stato = 'on'

    def spegni(self):
        self.stato = 'off'

    def setMarca(self, txt):
        self.marca = txt

l4 = Led3('rosso', 'on')
print(l4.colore)
l4.accendi()
print(l4.stato)
l4.spegni()
print(l4.stato)

print(l4)