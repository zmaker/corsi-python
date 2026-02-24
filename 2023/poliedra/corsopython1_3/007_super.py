class Rettangolo:
    def __init__(self, l, w):
        self.l = l
        self.w = w
    
    def area(self):
        return self.l * self.w

class Quadrato(Rettangolo):
    def __init__(self, l):
        super().__init__(l, l)
    
r = Rettangolo(10, 20)
print("A.R: ", r.area())
q = Quadrato(5)
print("A.Q: ", q.area())
        