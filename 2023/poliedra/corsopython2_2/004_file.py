f1 = open("dati.txt")
print(f1.read())

f1.seek(0)
print(f1.read())
print(f1.tell())

f1.seek(3)
print(f1.read())
f1.seek(0)

line = f1.readline()
print("linea: ", line)
line = f1.readline()
print("linea: ", line)

f1.seek(0)
for ll in f1:
    print("l: ", ll)

f1.close()

f2 = open("new.txt", "w")
f2.write("hello\n")
f2.write("file\n")
f2.close()

f2 = open("new.txt", "a")
f2.write("abc\n")
f2.close()

#f2.truncate()

import os

if os.path.exists("none.txt"):
    print("trovato")
else:
    print("non trovato")
    
if os.path.exists("empty.txt"):
    print("trovato: lo cancello")
    os.remove("empty.txt")
else:
    print("lo creo")
    f3 = open("empty.txt", "x")
    f3.close()


