'''
Mi faccio dare una lista di numeri
la stampo
la stampo al contrario

'''

n = int( input("quanti numeri? ") )

lista = []

for i in range(n):
    numero = int( input("n: ") )
    lista.append(numero)
    
for el in lista:
    print(el, end=" ")

print("\n")

for i in range(n):
    indice = n-1-i;
    print(lista[indice], end=" ")
'''
lunghezza lista = 4 
i     	4-i	4-1-i  n-1-i
0		4	3
1		3	2
2		2	1
3		1	0
'''
print("\nrev metodo 2")
for i in range(n, 0, -1):
    indice = i-1
    print(lista[indice], end=" ")

