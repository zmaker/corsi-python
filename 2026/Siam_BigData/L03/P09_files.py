f = open("dati.txt")
print(f.read())
f.seek(0)
print(f.read())
f.seek(3)
print(f.read())

f.seek(0)
line = f.readline()
print("l1", line)
line = f.readline()
print("l2", line)

f.seek(0)
for l in f:
    print(l, end='')

f.close()