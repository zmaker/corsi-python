class Forma():
    def __init__(self, l, w):
        self.l = l
        self.w = w

class Colorato():
    def __init__(self, colore):
        self.colore = colore
        
class Rettangolo(Forma, Colorato):
    def __init__(self, l, w, c):
        Forma.__init__(self, l, w)
        Colorato.__init__(self, c)
    
    def area(self):
        return self.l * self.w
    
    def perimetro(self):
        return (self.w + self.l) * 2
    
    def __str__(self):
        return f"Rettangolo {self.w}x{self.l}: {self.colore}"

class Quadrato(Rettangolo):
    def __init__(self, l):
        super().__init__(l,l)
        
r = Rettangolo(10, 20, "rosso")
print(r)

        