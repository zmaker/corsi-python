#ciclo for per ripetere operazioni e comandi

frutta = ['mela', 'banana', 'pera']

for elemento in frutta:
    # corpo del ciclo for
    # tutte le istruzioni da ripetere
    print(elemento)
   
numeri = [12, 23, 34, 45, 56]
for n in numeri:
    print(n, end=' ') # stampo senza andare a capo

#print("nel mezzo del\ncammin di nostra vita")

print("\n")
for c in "banana":
    print(c, end=' ')

print("\n")
#conteggio da 0 a 9 
for i in range(10):
    print(i, end=' ')

print("\n")
for i in range(1, 10):
    print(i, end=' ')
    
print("\n")
for i in range(0, 10, 2):
    print(i, end=' ')
    
# da 9 a 0    
print("\n")
for i in range(9, -1, -1):
    print(i, end=' ')
    
#stampo la lista frutta con un numero prima dell'elemento
print("\n")
p = 1
for el in frutta:
    print(p, el)
    #p = p + 1
    p += 1
    
