import numpy as np

dati = np.genfromtxt("2020-1.csv", delimiter=",")
print(dati.shape)
#escludo la prima riga
dati = dati[1:]

print(dati.shape)
print("caricati n. record:", dati.size)
righe = dati.size / 9
print("righe:", righe)

#stampo una riga
print(dati[1])
#estraggo colonna feriti
feriti = dati[:,7]
#estraggo colonna morti
morti = dati[:,8]

#print(feriti.shape)

totfer = np.sum(feriti)
totmor = np.sum(morti)
print("feriti: ", totfer)
print("morti: ", totmor)

np.save("datipuglia", dati)
