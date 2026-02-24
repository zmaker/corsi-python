def somma(a, b):
    return a + b

def diffe(a, b):
    return a - b

def molt(a, b):
    return a * b

def divi(a, b):
    if b == 0:
        return 0
    else:        
        return a / b

a = int(input("A: "))
b = int(input("B: "))
op = input("op [+-:x]: ")

res = 0
if op == '+':
    res = somma(a, b)
elif op == '-':
    res = diffe(a, b)
elif op == ':':
    res = divi(a, b)
elif op == 'x':
    res = molt(a, b)

print(res)

