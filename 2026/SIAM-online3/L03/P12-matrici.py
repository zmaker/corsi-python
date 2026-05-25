n = [1,2,3,4,5,6]

# matrice = tabella = lista di liste
m = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
print(m)
#estraggo la prima riga
print( m[0] )
#estraggo l'elemento centrale:
print( m[1][1] )
print( m[1][0] )

m[2][2] = 0
print(m)

#stampo la matrice
for r in range(3):
    for c in range(3):
        el = m[r][c]
        print(el, end=' ')
    print()

print()
q = [
    [1,2,3,4],
    [4,5,6,7],
    [7,8,9,0]
    ]
for r in range(3): #numero di righe
    for c in range(4): #numero di colonne
        el = q[r][c]
        print(el, end=' ')
    print()
    