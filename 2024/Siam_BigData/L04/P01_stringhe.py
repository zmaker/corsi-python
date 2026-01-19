# https://realpython.com/python-strings/

a = "Hello"
b = 'world'

c = a + ' ' + b
print(c)

d = 12

e = a + ' ' + b + " " + str(d)
print(e)

str = "John è \"strano\""
print(str)
str = 'John è \'strano\''
print(str)

scelte = "ABCDEF"
print(scelte[1])

testo = "nel mezzo del cammin di nostra vita"
print(testo[5:8])
print(testo[:3])
print(testo[:-2])

if "del" in testo:
    print("c'è")
    
n = testo.index("del")
print("n: ", n)

str = "     abc      "
print(str)
print(str.strip())

print(testo.upper())
print("Ciao Come Va?".lower())

print(testo.replace("e", "*"))
print(testo.replace("vita", "mela"))

dati = "12, 23,45,67,78,99"
nomi = "mela pera kiwi banana"

lista = nomi.split(" ")
print(lista)