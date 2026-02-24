import os.path

class CSV():
    def __init__(self, filename):
        
        self.filename = filename
        self.lines = list()
        
        if os.path.isfile(self.filename):            
            self.file = open(self.filename)
            
            line = self.file.readline()
            self.lines.append( Row(line) )
            
            while line:
                line = self.file.readline()
                self.lines.append( Row(line) )
            
            self.file.close()
            
        else:
            print("File non trovato")
    
    def getRowsCount(self):
        return len(self.lines)
    
    def __str__(self):
        txt = f"CSV File [{self.filename}]\n"
        for r in self.lines:
            txt += str(r) + "\n"
        return txt

    def getCell(self, r, c):
        rw = self.getRow(r)
        cc = rw.getCell(c)
        return cc.getValue()
    
    def getRow(self, n):
        return self.lines[n]

class Row():
    def __init__(self, txt):
        items = txt.split(sep=",")
        self.cells = []
        for el in items:
            self.cells.append( Cell(el) )
    
    def getCell(self, c):
        return self.cells[c]

    def __str__(self):
        txt = ""
        for el in self.cells:
            txt += str(el)
        return txt;

class Cell():
    def __init__(self, txt):
        self.value = txt.strip().replace('\n', '')
        
    def getValue(self):
        return self.value
    
    def __str__(self):
        return self.value.ljust(12)

if __name__ == "__main__":
    print("file di libreria - non eseguibile")