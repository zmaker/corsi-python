numeri = [10, 20, 30, 40, 50]
vuota = []
print(numeri)
print(numeri[0])

numeri[0] = 11
print(numeri)

numeri.append(99)
print(numeri)

print("elementi nella lista: ", len(numeri))

numeri.insert(3, 12)
print(numeri)

numeri.remove(99)
print(numeri)

l1 = [1, 2, 1, 1, 3]
print(l1)
l1.remove(1)
print(l1)

if 2 in l1:
    print("2 in lista")
if 5 in l1:
    print("5 in lista")

print("slicing")
print(numeri)
a = numeri[2:5]
print(a)

a = numeri[:3]
print(a)

a = numeri[3:]
print(a)

a = numeri[:-1]
print(a)

a = numeri[-1:]
print(a)

print("pop")
print(numeri)
el = numeri.pop()
print(f"elemento estratto con pop: {el}")
print(numeri)

tab = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
print(tab)
print(tab[1][0])

for n in numeri:
    print(n, end=' ')
    
    


    