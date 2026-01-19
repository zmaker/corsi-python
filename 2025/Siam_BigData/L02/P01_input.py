nome = input("come ti chiami? ")
anno = input("anno di nascita: ")
peso = int( input("peso? ") )

eta = 2024 - int(anno)
peso = peso * 0.6

print("ciao,", nome)
print("la tua età: ", eta)
print("peso sulla luna:", peso)

#stamp con template
print(f"Ciao, {nome} la tua età è di {eta - 2} e sulla luna pesi {peso} Kg ")