#insiemi
s1 = {2,4,6,8,10}
print("s1", s1 , type(s1))

lista = [1,2,2,2,3,4,5,5,6,7]
s2 = set(lista)
print("s2", s2)

s3 = set()
s3.add("mela")
s3.add("banana")
s3.add("cipolla")
print("s3", s3)

s3.discard("cipolla")
print("s3", s3)

if "banana" in s3:
    print("banana ok!")
    
# scorro gli elementi con un for
# l'ordine non è garantito    
for n in s1:
    print(n, end=" ")
print("") #va a capo dopo aver stampato la lista

a = {1,2,3,10,20}
b = {10,20,30,40,50}

c = a.union(b)
print("union", c)

c = a.intersection(b)
print("intersection", c)

c = a.difference(b)
print("diff 1", c)

c = b.difference(a)
print("diff 2", c)
