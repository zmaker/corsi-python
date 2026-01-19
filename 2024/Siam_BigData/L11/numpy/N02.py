import numpy as np

a = np.array([1,2,3,4])
b = np.array([1,1,1,1])

c = a + b
print(c)

A = a.reshape(2,2)
B = b.reshape(2,2)
C = A + B
print(C)

D = A * B
print(D)
D2 = np.matmul(A, B)
print(D2)

print(a)
print(a>2)
a*=2
print(a)

