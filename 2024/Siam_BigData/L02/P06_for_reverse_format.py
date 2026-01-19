for i in range(10):
    print(i, end=' ')
    
print("\nfor rovesciato")
for i in range(10, 0, -1):
    print(i, end=' ')

print("\nfloat() e str()")
n = int("123")
print(n)
n = float("123.45")
print(n)
print(str(123))

print("\nformat()")
n = 12.34567
print(format(n, '.2f'))
print(format(n, '.3f'))
print(format(n, '-8.3f'))
print(format(-n, '-8.3f'))
print(format(n, '08.3f'))
n = 123
print(format(n, 'b'))
print(format(n, 'x'))

input("premi invio per terminare")

print("fine del programma")