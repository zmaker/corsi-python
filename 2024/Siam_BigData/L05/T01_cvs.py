import csv
with open('file1.csv') as f:
    reader = csv.reader(f, delimiter=',')
    i = 0;
    for riga in reader:
        print(riga)
        i += 1
        if (i > 5):
            break;