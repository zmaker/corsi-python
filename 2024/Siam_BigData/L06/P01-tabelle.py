'''
OR
A B | O
----------
V V | V
V F | V 
F V | V
F F | F

'''
a = [True, False, True, False]
b = [True, True, False, False]

print("OR table")
print("A B | O")
print("--------")
for i in range(4):
    o = a[i] or b[i]
    print(f"{('T' if a[i] else 'F')} {('T' if b[i] else 'F')} | {('T' if o else 'F')}")
    
    
ingressi = [[0,0],[0,1],[1,0],[1,1]]
print("OR table")
print("A B | O")
print("--------")
for el in ingressi:
    o = bool(el[0]) or bool(el[1])
    print(f"{('T' if el[0] else 'F')} {('T' if el[1] else 'F')} | {('T' if o else 'F')}")

