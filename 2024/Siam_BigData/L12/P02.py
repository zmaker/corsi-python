import numpy as np

dati = np.genfromtxt("dati.csv")
print("caricati n. record:", dati.size)
print(dati)

aumento = dati * 1.20
np.savetxt('res.csv', aumento, fmt='%0.2f')

np.save('dati_app', aumento)

dati2 = np.load('dati_app.npy')
print(dati2)