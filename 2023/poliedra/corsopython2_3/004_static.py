class Led:
    
    contatore_led = 0
    
    def __init__(self, stato="OFF", colore="WHT"):
        Led.contatore_led += 1
        self.stato = stato
        self.colore = colore
        self.id = Led.contatore_led

l1 = Led()
print("id:", l1.id, "contatore_led:",  Led.contatore_led)
l2 = Led()
print("id:", l2.id, "contatore_led:",  Led.contatore_led)
l3 = Led()
print("id:", l3.id, "contatore_led:",  Led.contatore_led)
print("id l1:", l1.id)