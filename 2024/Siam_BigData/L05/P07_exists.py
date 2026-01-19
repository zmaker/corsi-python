import os

nomefile = 'test.txt'

if os.path.exists(nomefile):
    print(f"{nomefile} esiste: lo cancello")
    os.remove(nomefile)
    
else:
    print(f"creo {nomefile}")
    f = open(nomefile, 'x')
    f.close()
    
