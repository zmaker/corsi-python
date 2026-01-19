#file CSV

import csv

with open('impiegati.csv', 'w', newline='') as f:
    wr = csv.writer(f, delimiter=',')
    wr.writerow(['id','nome','telefono'])
    wr.writerow(['1','Mario','123456'])
    wr.writerow(['2','Luigi','455678'])
    wr.writerow(['3','Anna','767667'])
    
with open('impiegati.csv', 'r', newline='') as f:
    rd = csv.reader(f, delimiter=',')
    i = 0
    for riga in rd:
        if i == 0:
            print(riga[0], riga[1], riga[2])
            print("-------------------------")
        else:
            print(riga[0], riga[1], riga[2])
        i+=1

with open('impiegati.csv', 'r', newline='') as f:
    rd = csv.reader(f, delimiter=',')
    elenco = list(rd)
    
    print(elenco)