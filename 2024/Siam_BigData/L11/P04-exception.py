import random

class LetturaFuoriScala(Exception):
    def __init__(self, valore, message="Sensore fuori scala!!!"):
        self.valore = valore
        self.message = message
        super().__init__(self.message)
        
    def __str__(self):
        return f"ERRORE sensore: {self.valore}: fuori dai limiti!"

while True:
    val = random.randint(0, 100)
    print(val)
    if not 20 < val < 80:
        raise LetturaFuoriScala(val)