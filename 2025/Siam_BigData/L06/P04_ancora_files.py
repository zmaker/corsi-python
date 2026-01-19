f = open("testo1.txt")

linea = f.readline()
print(linea)

# riavvolgo il file
f.seek(0)

# leggo il file una riga per volta
for riga in f:
    print(riga, end='')
print("")

# riavvolgo il file
f.seek(0)

linee = f.readlines()
print(linee)

f.close()