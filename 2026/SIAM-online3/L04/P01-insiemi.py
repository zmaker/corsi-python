#tupla - sola lettura - parentesi tonde
t1 = (1,2,3)

#insiemi - {}
# operazioni booleane
a = {1, 2, 3, 4, 5}
b = {3, 5, 7, 9, 11}

# unione di insiemi
c = a.union(b)
print(c)

# intersezione di insiemi
d = a.intersection(b)
print(d)

#come elimino duplicati da una lista
n = [1,2,3,4,4,4,4,5,5,5,6,6,6]
m = set(n) #trasforma una lista in un insieme 
print(m)

#differenza di insiemi
e = a.difference(b)
print("e:", e)
f = b.difference(a)
print("f:", f)

#differenza simmetrica
g = a.symmetric_difference(b)
print("g:", g)