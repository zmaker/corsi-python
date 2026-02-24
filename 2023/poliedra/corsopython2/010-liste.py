numeri_lotto = [12, 45, 67, 4, 2]
frutta = ["mela", "pera", "banana"]
mista = ["mele", 2.01, 100, "fragole", 5.45, 20, "amazon"]

vuota = []

print(frutta)
print(frutta[1])
print(frutta[2])
frutta[2] = "fragola"
print(frutta)

vuota.append(2)
vuota.append(34)
print(vuota)

n = len(vuota)
print("elementi di lista vuota: ", n)

ll = [1,2,3,4,5,6,7,8]
print(ll)
ll.insert(2, 99)
print(ll)

lb = [100,200,300]
ll.extend(lb)
print(ll)

ll.remove(100)
print(ll)

if 1000 in ll:
    ll.remove(1000)
else:
    print(ll)
    
ll = [1,2,3,4,5,6,7,8,1]
ll.remove(1)
print(ll)

lx = [1,"1",3,4,5,6,7,8]
lx.remove(1)
print(lx)
lx.remove("1")
print(lx)

lx.pop()
print(lx)
lx.pop(2)
print(lx)

matrice = [[1,2,3],[11,22,33],[4,6,9]]

print("slice:", ll[3:6])
print("slice:", ll[3:])
print("slice:", ll[:5])
print("slice:", ll[:-2])

