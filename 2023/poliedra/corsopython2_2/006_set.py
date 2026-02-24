s1 = {0,2,4,6,8}
print(s1)

s2 = {"mele", "pere", "kiwi", "mele"}
print(s2)

l = [1,2,3,4,5,5,5,5]
s3 = set(l)
print(s3)

s2.add("pane")
print(s2)

if "pere" in s2:
    s2.remove("pere")

print(s2)

s2.discard("kiwi")
print(s2)
s2.discard("banane")

s2.clear()
print(s2)

A = {1,2,3,4,5}
B = {4,5,6,7,8}

C = A.union(B)
print("U:", C)

C = A.intersection(B)
print("I:", C)

C = A.difference(B)
print("D:", C)
C = B.difference(A)
print("D:", C)

C = A.symmetric_difference(B)
print("S:", C)

for el in A:
    print(el)






