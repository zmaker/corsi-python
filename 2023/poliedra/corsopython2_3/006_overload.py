class Led:
    def __init__(self, stato="OFF", colore="WHT"):
        self.stato = stato
        self.colore = colore

    def alimenta(self, i=0, v=0):
        pass

l1 = Led()
l1.alimenta()
l1.alimenta(i=1)
l1.alimenta(i=2, v=3)
