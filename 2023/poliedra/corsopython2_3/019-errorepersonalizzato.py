class LetturaFuoriScala(Exception):
    def __init__(self, valore, message="Valore fuori scala"):
        self.valore = valore
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f"{self.valore} fuori dei limiti"

while True:
    p = int(input("valore sensore: "))
    v = p / 3.14
    if p < 0 or p > 10:
        raise LetturaFuoriScala(p)
    print("lettura:", v)