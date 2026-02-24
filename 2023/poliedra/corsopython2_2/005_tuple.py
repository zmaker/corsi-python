l1 = [1,2,3]

t1 = (1,2,3)
t2 = ("mela","pera","kiwi")

t3 = ("mele", 100, 1.98)

print(t1)
print(t2)
print(t3)

for el in t2:
    print(el)
    
print("elemento 0:", t2[0])
print("elemento 1:", t2[1])

print("elementi: ", len(t2))

t4 = ("A", "B", "C", "A", "D")
print("count: ", t4.count("A"))

print("index: ", t4.index("B"))

print("X è in t4? ", "X" in t4)
print("B è in t4? ", "B" in t4)


#packing/unpacking
t5 = "pere", 120, 2.47
print(t5)

a, b, c = t5
print("a: ", a);
print("b: ", b);
print("c: ", c);

t6 = (1,2,3)
print(t6 * 2)
