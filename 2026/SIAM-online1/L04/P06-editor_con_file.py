'''
Text editor in Python - V2

utilizza file di testo
'''
import P06_mylib as mymod

#creo una lista vuota per memorizzare le righe di testo
righe = []

mymod.editorhelp()
while True:
    cmd = input("cmd? ")
    if (cmd == 'q'):
        break
    elif (cmd == 'h'):
        mymod.editorhelp()
    elif (cmd == 'i'):
        mymod.insertline(righe)
        mymod.printbuffer(righe)
    elif (cmd == 'p'):
        mymod.printbuffer(righe)
    elif (cmd == 'c'):
        mymod.clearbuffer(righe)
    elif (cmd == 'o'):
        mymod.openFile(righe)
    elif (cmd == 's'):
        mymod.saveFile(righe)
    else:
        print("?")