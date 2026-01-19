#leggo un file di testo

f = open("testo1.txt")

print(f.read())

#riavvolgo il file come se fosse un nastro
f.seek(0)
print(f.read())

f.seek(0)
print(f.read(3))

f.seek(0)
print(f.read())

num_caratteri_letti = f.tell()
print("ho letto:", num_caratteri_letti, "caratteri")

f.close()