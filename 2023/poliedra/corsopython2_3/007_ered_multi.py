class Forma:
    def __init__(self, l, w):
        self.l = l
        self.w = w
    
    def area(self):
        print(self.l * self.w)
        
class Colorato:
    def __init__(self, c):
        self.colore = c
        
class Rect(Forma):
    def __init__(self, l, w):
        super().__init__(l, w)
        
class Quad(Rect):
    def __init__(self, l):
        super().__init__(l,l)
        
r = Rect(10, 12)
r.area()
q = Quad(10)
q.area()
        
    
        