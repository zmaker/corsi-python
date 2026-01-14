frutta = ['mela', 'pera', 'kiwi', 'banana']

for el in frutta:
    #corpo del ciclo for
    print(el)

numeri = [12,23,34,45,56]
somma = 0
for n in numeri:
    somma += n
    print(n, end=' ')

print()
print("somma: ", somma)

for ch in "banana":
    print(ch, end=" ")
    
print()    
for n in range(0,10):
    print(n, end=" ")
    
print()    
for n in range(0, 10, 2):
    print(n, end=" ")
    
print()    
for n in range(9, -1, -1):
    print(n, end=" ")
    
print()
i = 0
for el in frutta:    
    print(i, el)
    i += 1

print()
for i, el in enumerate(frutta):    
    print(i, el)
    
    