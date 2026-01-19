'''
Text editor in Python

- riceve una riga di testo per volta
- memorizza le righe di testo in una lista
- visualizzo il testo
- posso eliminare una riga di testo
extra
- inserisco una riga di testo in una posizione a piacere
'''
import mymod
#mymod.test()

#from mymod import saluta
#saluta()
#from mymod import saluta as bye
#bye()

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
    else:
        print("?")