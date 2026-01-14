m = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

print(m)
print(m[0][1])

m[1][1] = 0
print(m)
print()

for r in range(3):
    for c in range(3):
        el = m[r][c]
        print(el, end=' ')
    print()