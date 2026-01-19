def somma(a,b):
    pass
def diff(a,b):
    pass
def prod(a,b):
    pass
def div(a,b):
    pass

while (True):
    ans = input("che operazione? ")
    a = float(input("primo numero: "))
    b = float(input("secondo numero: "))
    if not ans:
        break
    elif ans == '+':
        somma(a, b)
    elif ans == '-':
        diff(a, b)
    elif ans == '*':
        prod(a, b)
    elif ans == '/':
        div(a, b)
    else:
        print("???")