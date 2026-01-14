numeri = [12, 23, 34 ,56, 67]
print(numeri)

print("primo el: ", numeri[0])
i = 2
print("primo el: ", numeri[i])

numeri[2] = 99
print(numeri)

print("elementi nella lista", len(numeri))

mag = ["mele", 12, 0.98, "pere", 100, 1.23]
print(mag)

l1 = []
print(len(l1))

l1.append(1)
l1.append(2)
l1.append(3)

print(l1)

l1.pop()
print(l1)

print(numeri)
numeri.pop(2)
print(numeri)

print(mag)
mag.remove("mele")
print(mag)

el = "kiwi"
if el in mag:
    mag.remove(el)
    print(mag)
else:
    print(el, "non presente")
    
#     0   1   2   3   4   5   6
n = [12, 23, 34, 45, 56, 67, 78, 89, 90, 87, 67]
print("\nlista n", n)
print( n[2:4] )
print( n[:4] )
print( n[5:] )

print( n[-1] )

txt = "hello world"
print(txt[1])
print(txt[1:5])




