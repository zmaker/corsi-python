import numpy as np

a1 = np.array([1,2,3,4,5,6,7,8,9])
print(a1, type(a1), a1.shape)

m1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(m1, type(m1), m1.shape)

a1.shape=(3,3)
print(a1, "shape:", a1.shape)

a2 = np.array([1,2,3,4,5,6,7,8,9,10])
print("a2\n", a2, "shape:", a2.shape)
a3 = a2.reshape(2,5)
print("a3", a3, "shape:", a3.shape)

print("tipo di dato di a3", a3.dtype)

a4 = np.array([1,2,3,4.0,5,6,7,8,9])
print("tipo di dato di a4", a4.dtype)

a5 = np.array([1,2,3,4,5,6,7,8,9,10], np.uint8)
print("tipo di dato di a5", a5.dtype)