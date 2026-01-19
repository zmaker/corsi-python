#Campo Minato

dx = 5
dy = 5

def getCell(fld, x,y):
    global dx,dy
    return fld[(dx*y) + x]

def setCell(fld, x,y, val):
    global dx,dy
    fld[(dx*y) + x] = val

def main():    
    campo = [0 for i in range(dx*dy)]
    print(campo)
    print(getCell(campo, 4,1))
    
    

if __name__ == '__main__':
    main()