f = open("testo1.txt")
print(f.read(3))
f.seek(0)
print(f.read())

num_caratteri = f.tell()
print("caratteri letti: ", num_caratteri)

f.close()

