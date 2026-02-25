class Calc():
    
    def __init__(self):
        self.result = 0
    
    def setOperando1(self, n):
        self.op1 = int(n)
    
    def setOperando2(self, n):
        self.op2 = int(n)
    
    def setOperatore(self, op):
        self.op = op
    
    def getResult(self):
        self.calcola()
        return self.result

    def calcola(self):
        if (self.op == '+'):
            self.result = self.op1 + self.op2
        elif (self.op == '-'):
            self.result = self.op1 - self.op2
        elif (self.op == 'x'):
            self.result = self.op1 * self.op2
        elif (self.op == ':'):
            self.result = self.op1 / self.op2
        elif (self.op == '%'):
            self.result = self.op1 % self.op2
        else:
            self.result = 0
            
    def __str__(self):
        return f"{self.op1} {self.op} {self.op2} = {self.result}"
    
if __name__ == "__main__":
    print("non eseguibile")