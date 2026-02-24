s1 = {"a", "b", "m", "n", "c"}
print(s1)

s2 = {"a", "b", "a", "c", "a"}
print(s2)

lista = ["mele", "pere", "fragole", "mele"]
s3 = set(lista)
print(s3)

s3.add("kiwi")
print(s3)

s4 = {"a", "b", "m", "n", "c"}
print("s4 prima:", s4)
s4.discard("m")
print("s4 dopo:", s4)

s5 = {"a", "b", "m", "n", "c"}
print("s5 prima:", s5)
if "x" in s5:
    s5.remove("x")
print("s5 dopo:", s5)

s5.clear()
print("s5 vuoto", s5)

A = {1,2,3,4,5}
B = {4,5,6,7,8}
C = A.union(B)
print("unione: ", C)

D = A.intersection(B)
print("inter: ", D)

E = A.difference(B)
print("diff A-B: ", E)
F = B.difference(A)
print("diff B-A: ", F)

G = A.symmetric_difference(B)
print("sdiff: ", G)

for el in A.union(B):
    print(el)

