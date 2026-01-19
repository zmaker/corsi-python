import numpy as np

n = np.random.random((10,))*100
print("n", n)

r = n[n>50]
print("r",r)

# AND uso &
# OR uso |
r = n[(n>20) & (n<80)]
print("r",r)

n = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
m = np.where(n < 5, n, 0)
print(m)
m = np.where(n >= 5, "ALTO", "BASSO")
print(m)
#cerco posizione
r = np.where(n == 5)
print(r, "posizione cercata: ", r[0][0])

n = np.array([0, 1, 5, 3, 4, 5, 6, 7, 5, 9])
r = np.where(n == 5)
print(r, "posizione cercata: ", r[0])

r = np.where(n == 99)
#lista dei risultati trovati
lres = r[0]
print(lres)
#analizzo le dim di lres
print(len(lres))
print(r, "posizione cercata: ")