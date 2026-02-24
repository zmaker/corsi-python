class Forma:
    def __init__(self, l, w):
        self.l = l
        self.w = w
    
    def area(self):
        print(self.l * self.w)
        
class Colorato:
    def __init__(self, c):
        self.colore = c
    
    def getColor(self):
        return self.colore
        
class Rect(Forma, Colorato):
    def __init__(self, l, w, c):
        Forma.__init__(self, l, w)
        Colorato.__init__(self, c)
        
class Quad(Rect):
    def __init__(self, l, c):
        super().__init__(l,l, c)
        
r = Rect(10, 12, "rosso")
r.area()
print(r.getColor())
q = Quad(10, "giallo")
q.area()
print(q.getColor())
    
        
