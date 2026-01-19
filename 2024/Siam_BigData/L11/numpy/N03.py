import numpy as np

a = np.arange(0,9).reshape(3,3)
print(a)

b = np.random.random((3,3))*100
print(b)

#array vuoto
v = np.empty((5,5))
print(v)

c = np.zeros( (4,4))
print(c)
d = np.ones((3,3))
print(d)
e = np.full((3,3), 5)
print(e)
e = np.full((3,3), 'Hi')
print(e)
e = np.full((3,3), False)
print(e)

f = np.linspace(1, 100, num=10)
print(f)

print(f[0])
print(b)
print(b[0][1])

n = np.array([1,2,3,4,5,6,7,8,9])
print(n)
print(n[-1])
print(n[3:6])
print(n[:6])
print(n[5:])

m = np.array([1,2,3,4,5,6,7,8,9]).reshape(3,3)
print("m", m)
print(m[1][2])
print(m[1])
print(m[:,0])

n = np.array([1,2,3,4,5,6,7,8,9])
print("\nappend", n)
n1 = np.append(n, 99)
print(n1)

print("\ninsert", n)
n2 = np.insert(n, 3, 99)
print(n2)