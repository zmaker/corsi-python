s1 = {'a', 'b', 'c', 'd'}
print("s1", s1, type(s1))

s2 = {'a', 'b', 'c', 'd', 'a'}
print("s2", s2)

lista = ['a', 'b', 'c', 'd', 'a', 'b']
s3 = set(lista)
print("s3", s3)

s3.add('x')
print("s3", s3)

s3.discard('x')
print("s3", s3)

#remove() da errore
#s3.clear()

if "c" in s3:
    print("OK C")
    
for el in s3:
    print(el)
    
a = {1, 2, 3, 4, 10}
b = {10, 20, 30, 40}
c = a.union(b)
print(c)

d = a.intersection(b)
print(d)

e = a.difference(b)
print(e)

e = b.difference(a)
print(e)

