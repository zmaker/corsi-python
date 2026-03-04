m = [[1,2,3],
    [4,5,6],
    [7,8,9]]

print(m)
print("estraggo la prima riga: ", m[0])
print("estraggo il secondo el della prima riga: ", m[0][1])

for r in range(3):
    # estraggo le righe
    for c in range(3):
        el = m[r][c]
        print(el, end=' ')
    print("")
