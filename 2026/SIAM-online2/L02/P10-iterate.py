# enumerate

nomi = ["anna", "max", "bob", "alice"]
p = 1
for n in nomi:
    #print(p, ".",  n)
    print(f"{p}. {n}")
    p += 1
    
for i, n in enumerate(nomi):
    print(f"{i}) {n}")