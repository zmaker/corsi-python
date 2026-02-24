#csv_reader_lib.py
import os.path

class CSV:
    def __init__(self, filename):
        self.filename = filename
        self.lines = list()
        self.rows = 0
        
        if os.path.isfile(self.filename):
            self.file = open(self.filename)            
            line = self.file.readline()
            self.lines.append(Row(line))
            while line:
                line = self.file.readline()
                self.lines.append(Row(line))
                
            self.file.close()
            self.rows = len(self.lines)
            
        else:
            print("File non trovato!")
            
    def getRowsCount(self):
        return self.rows
    
    def getRow(self, n):
        return self.lines[n]
    
    def getCell(self, r, c):
        rw = self.getRow(r)
        c = rw.getCell(c)
        return c.getValue()
        
    def __str__(self):
        txt = f"CSV[{self.filename}]\n"
        for r in self.lines:
            txt += str(r) + "\n"
        return txt
    
class Row:
    def __init__(self, txt):
        #mele,10,1.98
        items = txt.split(sep=",")
        self.cellnum = 0
        self.cells = []
        
        for el in items:
            self.cells.append(Cell(el))
            self.cellnum += 1
    
    def getCell(self, n):
        return self.cells[n]
    
    def __str__(self):
        txt = ""
        for el in self.cells:
            txt += str(el)
        return txt

class Cell:
    def __init__(self, txt):
        self.value = txt.strip().replace('\n', '')
    
    def getValue(self):
        return self.value
    
    def __str__(self):
        return self.value.ljust(12)

if __name__ == '__main__':
    print("Non eseguibile")