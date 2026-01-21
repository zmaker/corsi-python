import csv

with open("magazzino.csv", "w") as f:
    cur = csv.writer(f, delimiter=",")
    cur.writerow(['cod', 'nome', 'eta'])
    cur.writerow([1, 'mario', 23])
    cur.writerow([2, 'luigi', 27])
    cur.writerow([3, 'anna', 24])