print("Super calc!")
a = input("primo numero: ")
b = input("secondo numero: ")
a = int(a)
b = int(b)
somma = a + b
prod = a * b
diff = a - b
div1 = a / b
div2 = a // b
modulo = a % b
potenza = a ** b

print(f"{a} + {b} = {somma}")
print(f"{a} x {b} = {prod}")
print(f"{a} - {b} = {diff}")
print(f"{a} / {b} = {div1}")
print(f"{a} / {b} = {div2} divisione intera (senza virgola)")
print(f"Resto di {a} / {b} = {modulo} resto della divisione")
print(f"{a} elevato a {b} = {potenza}")