# ex. - Calcolatrice
# chiedo due numeri
print("Calcolatrice\nDammi due numeri:")
a = int(input("A? "))
b = int(input("B? "))

# chiedo che operazione si desidera svolgere
print("che operazione? (+ somma, - sottrazione, x molt...)")
op = input("operazione: ")

# scelgo l'operazione in base alla risposta
# e stampo il risultato
res = 0
if (op == '+'):
    res = a + b
    print(f"{a} + {b} = {res}")
elif (op == '-'):
    print(f"{a} - {b} = {a-b}")
else:
    print("Operazione non prevista")