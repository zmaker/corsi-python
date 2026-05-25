#insiemi
s = {'a', 'b', 'c', 'd'}
print(s)

s1 = {}
print(s1)

n = [1,2,3,4,5]
s1 = set(n)
print(s1)

s1.add(9)
print(s1)
s1.add(8)
print(s1)

s1.add(9)
s1.add(9)
s1.add(9)
print(s1)

s1.discard(9)
print(s1)

s1.discard(99)
print(s1)

if 99 in s1:
    s1.remove(99)
    
for el in s1:
    print(el, end=" ")
print()
    
