import numpy as np

prezzi = np.array([12,23,45,56,67,78,89,90,24,35,46,57,68])

print("min:", np.amin(prezzi))
print("max:", np.amax(prezzi))
print("media:", np.average(prezzi))
print("var:", np.var(prezzi))
print("dev std:", np.std(prezzi))
print("range valori:", np.ptp(prezzi))
print("somma:", np.sum(prezzi))

indici = np.array([np.average(prezzi), np.var(prezzi), np.std(prezzi)])
print(indici)
indici2 = np.around(indici, 2)
print(indici2)
print(np.ceil(indici2))
print(np.floor(indici2))
