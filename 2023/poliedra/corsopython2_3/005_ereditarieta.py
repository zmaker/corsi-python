class Auto:
    def __init__(self, color, year):
        self.color = color
        self.year = year
        self.speed = 0
    
    def setSpeed(self, speed):
        self.speed = speed
        
    def beep(self, suono):
        return f"((({suono})))"
    
    def __str__(self):
        return f"[Auto, c:{self.color} ]"
    
class Fiat500(Auto):
    def __str__(self):
        return f"[500 di un bel colore {self.color} ]"
    
class Perrari(Auto):
    def __str__(self):
        return f"[Perrari {self.color} ]"

    def beep(self, suono="BOOOOO"):
        return f"Perrari says: {suono}"

a = Fiat500("blu", "2015")
p = Perrari("rossa", "1997")

print("clacson perrari: ", p.beep())
print("clacson 500: ", a.beep("bip"))

print(a)
print(p)


print("e' una Perrari?", isinstance(p, Perrari))
print("e' una Perrari?", isinstance(a, Perrari))
print("e' una Auto?", isinstance(p, Auto))
