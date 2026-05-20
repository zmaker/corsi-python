n = int(input("quanti oggetti ti servono? "))

lista_spesa = []

for i in range(n):
    nome = input("oggetto: ")
    lista_spesa.append(nome)

print(lista_spesa)