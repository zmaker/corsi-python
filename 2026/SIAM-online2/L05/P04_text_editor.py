'''
EX01 - Editor di testi
'''
'''
tre modi per importare moduli e funzioni da moduli esterni
import editor_mod as ed
ed.test()

from editor_mod import test
test()

from editor_mod import test as prova
prova()
'''

import editor_mod as ed

righe = []
filename = 'doc1.txt'

print("Minimal PyEditor")
ed.help()

while True:
    cmd = input("cmd: ")
    if (cmd == 'q'):
        break
    elif (cmd == 'h'):
        ed.help()
    elif (cmd == 'i'):
        ed.insert(righe)
    elif (cmd == 'p'):
        ed.prt(righe)
    elif (cmd == 'c'):
        ed.clr(righe)
    elif (cmd == 's'): #save file
        ed.save(filename, righe)
    elif (cmd == 'o'): #open file
        ed.clr(righe)
        ed.load(filename, righe)
        ed.prt(righe)
