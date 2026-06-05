import os

# import P01_Editor_library -> import secco
# P01_Editor_library.test()

'''
import P01_Editor_library as mylib #import con alias
mylib.test()

from P01_Editor_library import test
test() 

from P01_Editor_library import test as t1
t1()
'''

import P01_Editor_library as ed

righe = []
filename = "doc1.txt"

# stampo le istruzioni 
ed.help()

while True:
    cmd = input("cmd: ")
    if (cmd == 'q'):
        break
    elif (cmd == 'h'):
        ed.help()
    elif (cmd == 'i'):
        ed.getLine(righe)
    elif (cmd == 'p'):
        ed.prt(righe)  
    elif (cmd == 'o'):
        ed.readFile(filename, righe)
    elif (cmd == 's'):
        ed.saveFile(filename, righe)
    elif (cmd == 'c'):
        righe.clear()
        print("buffer svuotato")
    else:
        print("???")    