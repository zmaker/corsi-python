from P02_lib import SimpleEditor

def main():
    filename = 'doc1.txt'
    
    ed = SimpleEditor()
    ed.help()

    while True:
        cmd = input("cmd: ")
        if (cmd == 'q'):
            break
        elif (cmd == 'h'):
            ed.help()
        elif (cmd == 'i'):
            ed.insert()
        elif (cmd == 'p'):
            ed.prt()
        elif (cmd == 'c'):
            ed.clr()
        elif (cmd == 's'): #save file
            ed.save(filename)
        elif (cmd == 'o'): #open file
            ed.clr()
            ed.load(filename)
            ed.prt()


if __name__ == "__main__":
    main()