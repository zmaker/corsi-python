# Stringhe in Python

a = "Hello"
b = 'World'

c = a + ' ' + b
print(c)

n = 12
e = "n vale: " + str(n)
print(e)

#conversioni di tipo - typecast
# str()
# int()
# float()
# bool()

# msg = "John è "strano"" ERRORE
msg = "John è 'strano'"
print(msg)
msg = 'John è "strano"'
print(msg)
msg = "John è \"strano\""
print(msg)

scelte = "ABCDEF"
print(scelte[1])

for x in scelte:
    print(x, end=' ')
print("")

#slicing - prendere una parte della stringa (o lista di caratteri)
# substring
testo = "era una notte buia e tempestosa..."
print(testo[4:9]) #una parte della stringa: da .. a
print(testo[10:]) #dall'indice 10 alla fine
print(testo[:10]) #dall'inizio all'indice 10
print(testo[-4])  #il quart-ultimo carattere del testo
print(testo[-3:]) #gli utlimi 3 caratteri del testo

#verifico se una parola è contenuta in un testo
if 'notte' in testo:
    print("trovata!")

#voglio conoscere la posizione di una parola all'interno di una stringa
pos = testo.index('notte')
print(pos)

#rimuovere spazi non necessari
saluto = "     ciao      "
saluto = saluto.strip()
print(saluto)
saluto = "     Ciao  Mondo    "
saluto = saluto.strip()
print(saluto)

print(saluto.upper())
print(saluto.lower())

src = input("cosa cerco? ")
if src.upper() in saluto.upper():
    print("trovato ciao")
else:
    print("non trovato ciao")

msg = "nel mezzo del cammin di nostra vita"
print(msg.replace('e', 'u'))
print(msg.replace("vita", "mela"))

dati = "12, 34,   56,57 ,  9 , 12"
lista = dati.split(",")
print(lista)
lista_pulita = []
for n in lista:
    numero = int(n.strip())
    print(numero, end=" ")
    lista_pulita.append(numero)
print(" ")
print(lista_pulita)

nomi = "mela pera banana kiwi"
lista_nomi = nomi.split(" ")
print(lista_nomi)
