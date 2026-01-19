def sommaLinea(dati):
    #codice che somma i numeri trovati dentro a dati
    lista = dati.split(',')
    lista_pulita = []
    for n in lista:
        #tolgo gli spazi in eccesso
        num = n.strip()
        #trasformo in numero
        num = int(num)
        #salvo il num nella nuova lista
        lista_pulita.append(num)

    print(lista_pulita)

    somma = 0
    for n in lista_pulita:
        somma = somma + n

    print("somma:", somma)
    
f = open("numeri.txt")

for linea in f:
    linea = linea.replace('\n', '')
    #print(linea)
    sommaLinea(linea)

f.close()