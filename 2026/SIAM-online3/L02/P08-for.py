# ciclo for per ripetere operazioni un nuumero prefissato di volte

frutta = ['mela', 'pera', 'kiwi']

for elemento in frutta:
    print(elemento)
    print(elemento.upper())

numeri = [12, 23, 34, 45, 56]
for n in numeri:
    print(n, end=' ')
print()    

numeri = [12, 23, 34, 45, 56, 100, 200]
somma = 0
for n in numeri:
    #somma = somma + n
    somma += n

print(somma)

#ciclo for per fare un conteggio
for i in range(10):
    print(i*i, end=" ")
print()

for i in range(3,10):
    print(i, end=" ")
print()

for i in range(2,20,3):
    print(i, end=" ")
print()

for i in range(9,-1, -1):
    print(i, end=" ")
print()



    