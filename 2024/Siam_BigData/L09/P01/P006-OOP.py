class Rettangolo:
    def __init__(self, h, w):
        self.h = h
        self.w = w

    def __str__(self):
        return f"R[{self.w}x{self.h}]"

    def area(self):
        return self.h * self.w

class Quadrato(Rettangolo):
    def __init__(self, l):
        super().__init__(l, l)

r1 = Rettangolo(10,20)
print("area:", r1.area())

q1 = Quadrato(10)
print("area:", q1.area())