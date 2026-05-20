'''
creare un programma che chiede alcuni dati all'utilizzatore:
- nome
- cognome
- anno di nascita

stampate i dati a video
e l'età.
'''

#chiedo il nome
nome = input("nome: ")

#chiedo il cognome
cognome = input("cognome: ")

#chiedo anno di nascita
anno = int( input("anno nascita: ") )

#calcolo eta
eta = 2026 - anno

#stampo i risultati
print("ciao: ", nome, " ", cognome)
print("hai: ", eta, "anni")
#stampa con template / maschera
print(f"Ciao, {nome}, {cognome}. Eta: {eta+1}")

