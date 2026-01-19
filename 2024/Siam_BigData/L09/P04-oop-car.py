class Automobile:
    def __init__(self, colore, targa):
        self.colore = colore
        self.marca = "XYZ"
        self.targa = targa
        self.fuel = 0
        self.x = 0
    
    def __str__(self):
        return f"Auto: {self.colore} x:{self.x} f:{self.fuel}"

    def __del__(self):
        pass

    def addFuel(self):        
        if (self.fuel < 5):
            self.fuel += 1;

    def move(self):
        if self.fuel > 0:
            self.x += 1
            self.fuel -= 1
        else:
            print("fai rifornimento")

c1 = Automobile("red", "AB123AC")
print(c1)
for i in range(10):
    c1.addFuel()
print(c1)

c1.move()
print(c1)
c1.move()
print(c1)