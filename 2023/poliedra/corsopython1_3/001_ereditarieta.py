class Auto:
    def __init__(self, c, y):
        self.color = c
        self.year = y
        self.speed = 0
        self.marcia = 0
        self.acceleratore = 0
    
    def setSpeed(self, s):
        self.speed = s
        
    def beep(self, s):
        return f"- {s} )))"
        
    def go(self, marcia=1, acceleratore=0):
        self.marcia = marcia
        self.acceleratore = acceleratore
    
    def __str__(self):
        return f"[Auto] c:{self.color} y:{self.year} s:{self.speed} go:{self.marcia}@{self.acceleratore}"

class Fiat500(Auto):
    def beep(self, s):
        return f"Il clacson della 500 fa {s}"

class Perrari(Auto):
    def beep(self, s="BEEEEEP"):
        return f"Il clacson della Perrari fa {s}"
    
    def __str__(self):
        return f"[Perrari] c:{self.color} y:{self.year} s:{self.speed}"

f = Perrari("rossa", 1997)
c = Fiat500("blu", 2018)
print(f.beep())
print(c.beep("beep!"))

print(f)
print(c)

print("e' una Perrari: ", isinstance(f, Perrari))
print("e' una Auto: ", isinstance(f, Auto))
print("e' una Fiat500: ", isinstance(f, Fiat500))

c.go()
c.go(1)
c.go(2, 50)

