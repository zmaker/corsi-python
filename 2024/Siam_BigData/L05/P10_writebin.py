nomefile = 'dati.bin'

numeri = [10, 20, 30, 1 , 2, 3]

with open(nomefile, 'wb') as f:
    arr = bytearray(numeri)
    f.write(arr)


with open(nomefile, 'rb') as f:
    dati = f.read()
    for el in dati:
        print(el)
    