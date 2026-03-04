# insiemi
s = {'a', 'b', 'c', 'd'}
print(s)

s1 = {}
print(s1)

n = [1,2,3,4,5]
s1 = set(n)
print(s1)

s1.add(9)
print(s1)
s1.add(9)
print(s1)

#elimino un elemento con discard()
s1.discard(9)
print(s1)

s1.discard(99)
print(s1)

if 99 in s1:
    s1.remove(99)
else:
    print("non presente")
    
# svuoto un insieme con clear()
s1.clear()
print(s1)

#scorro glielementi di u ninsieme con for
print(s)
for el in s:
    print(el, end=' ')
print("")

#operazioni con gli insiemi
a = {1,2,3,4,5,6,7,8,9}
b = {6, 8, 9, 10, 20, 30}

#unione degli insiemi a e b
c = a.union(b)
print(c)

#intersezione
d = a.intersection(b)
print(d)

#differenza
e = a.difference(b)
print(e)
f = b.difference(a)
print(f)

#differenza simmetrica
g = a.symmetric_difference(b)
print(g)