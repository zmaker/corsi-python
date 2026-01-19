f = open("testo2.txt")

riga = f.readline()
print("riga1", riga)

riga = f.readline()
print("riga2", riga)

riga = f.readline()
print("riga3", riga)

#riavvolgo
f.seek(0)
print("\n\nlettura con for ---------")
i = 0
for row in f:
    print(i, row, end='')
    i += 1

#riavvolgo
f.seek(0)
print("\n\nlettura blocco linee ---------")
linee = f.readlines()
i = 0
for row in linee:
    print(i, row, end='')
    i += 1


f.close()


