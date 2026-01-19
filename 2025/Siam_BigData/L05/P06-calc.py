def somma(a, b):
    s = a + b
    print(f"{a} + {b} = {s}")
    
def diff(a, b):
    s = a - b
    print(f"{a} - {b} = {s}")

while (True):
    op = input("che operazione (+,-,x,/): ")
    a = float(input("primo numero: "))
    b = float(input("secondo numero: "))

    if (op == '+'):
        somma(a, b)
    elif (op == '-'):
        diff(a, b)
    else:
        break;
