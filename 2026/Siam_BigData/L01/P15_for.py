frutta = ['mele', 'pere', 'kiwi']

for el in frutta:
    #corpo del ciclo
    #istruzioni da ripetere
    print(el)
    
temp = [12, 23, 34, 45, 56, 67, 78, 89]
somma = temp[0] + temp[1] + temp[2] + temp[3] +temp[4]
print(somma)

somma = 0
for n in temp:
    somma = somma + n

print("somma con for: ", somma)

print("for da 0 a 9")
for i in range(10):
    print(i, end=' ')

print()
print("for da 10 a 1")
for i in range(10, 0, -1):
    print(i, end=' ')
print()

numero_nomi = int( input("quanti nomi?"))
n = []
for i in range(numero_nomi):
    print(i, end=' ')
    nome = input("nome? ")
    n.append(nome)
print(n)
