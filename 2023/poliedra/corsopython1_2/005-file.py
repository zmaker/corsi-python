file1 = open("dati.txt")
print(file1.read())

file1.seek(0)
print(file1.read())

file1.seek(2)
print(file1.read())

#leggo una linea
file1.seek(0)
l1 = file1.readline()
print("linea 1: ", l1, end="")
l1 = file1.readline()
print("linea 2: ", l1)

file1.seek(0)
i = 1
for l in file1:
    print(i, ": ", l, end="")
    i += 1
    
#scrittura
file2 = open("out.txt", "w")
file2.write("dato1\n")
file2.write("temp= 12\n")
file2.close()
#file2.truncate()
file2 = open("out.txt")
print("\nlettura file:")
print(file2.read())
file2.close()

#append
file2 = open("out.txt", "a")
file2.write("hum=100%\n")
file2.close()

file2 = open("out.txt")
print("\nlettura file:")
print(file2.read())
file2.close()

import os
import time
file4 = open("new.txt", "x")
file4.close()
time.sleep(3)
os.remove("todel.txt")


if os.path.exists("todel.txt"):
    os.remove("todel.txt")
    print ("rimosso")
else:
    print ("non trovato")
    
#creo file
if not os.path.exists("new.txt"):
    file3 = open("new.txt", "x")
    file3.close()





