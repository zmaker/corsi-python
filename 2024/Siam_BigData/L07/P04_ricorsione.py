def f(n):
    print(n, end=' ')
    if n > 0:
        f(n-1)
    else:
        return 0

def fatt(n):
    #print(n, end=' ')
    if n == 1:
        return 1
    else:
        return n * fatt(n-1)

def fsum(n):
    #print(n, end=' ')
    if n == 1:
        return 1
    else:
        return n + fsum(n-1)

    
#f(5)
n = fatt(5)
print("fattoriale:", n)

n = fsum(3)
print("somma fatt:", n)
