'''
ciclo for - per ripetere operaioni
ideale se conosco prima il numero di ripetizioni (iterazioni)
'''
frutta = ['mela', 'pera', 'banana', 'kiwi']

for el in frutta:
    #corpo del ciclo
    #istruzioni che ripeto
    print(el)
    
numeri = [12,23,34,45,56,67,78]
for n in numeri:
    print(n, end=' ')
    
#vado a capo
print("\n")

frutto = "banana"
for c in frutto:
    print(c, end=" ")

print("\n")

for n in range(0,10):
    print(n, end = " ")

print("\n")

for n in range(20):
    print(n, end = " ")

print('\n')
'''
for x in range(ord('a'), ord('z')+1):
    print(x, chr(x))
'''

for n in range (0, 20, 2):
    print(n, end=' ')
    
print('\n')
for n in range (9, -1, -1):
    print(n, end=' ')
