nomi = ["mario", "max", "luisa", "luigi"]
voti = [6,7,8,9]

p = 1
for n in nomi:
    print(p, n, voti[p-1])
    p += 1

print("\nlista con enumerate:")
for i, n in enumerate(nomi):
    print(i, n, voti[i])
    
print("\n")
for i, n in enumerate(voti):
    print((i+1), nomi[i], n)
