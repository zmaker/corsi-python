print("Valutazione scuola secondaria\n")
print("Media dei voti in materia XX?")

voto = int(input("Numero tra 0 e 10: "))

if 0 <= voto <= 5:
    print("bocciato")

elif voto == 6:
    print("rimandato a settembre")

elif voto == 7:
    print("promosso_sufficiente")

elif voto == 8:
    print("promosso_buono")

elif voto == 9:
    print("promosso_molto_buono")

elif voto == 10:
    print("promosso_ottimo")

else:
    print("numero NON valido")