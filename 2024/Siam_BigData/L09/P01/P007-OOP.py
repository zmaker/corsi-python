class Forma:
    def __init__(self, w, h):
        self.w = w
        self.h = h

class Colorato:
    def __init__(self, colore):
        self.colore = colore


class Rect(Forma):
    def __init__(self, l, a):
        super().__init__(l, a)

    def area(self):
        return self.h * self.w

    def perimetro(self):
        return 2*(self.h + self.w)

class Quadrato(Rect, Colorato):
    def __init__(self, l):
        self.l = l
        Rect.__init__(self, self.l, self.l)
        Colorato.__init__(self, "nero")

    def __str__(self):
        return f"Q[{self.l}x{self.l}] c: {self.colore}"

q = Quadrato(10)
print(q)
