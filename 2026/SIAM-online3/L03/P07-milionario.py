domande = [
    "Quale di queste affermazioni sulla balena è falsa?",
    "Cos'è l'abacà?",
    "Se a San Francisco vedo il Golden Gate, cosa sto osservando?"
    ]

scelte = [
    ["ha i fanoni","è un cetaceo","ha 2 figli per volta","si nutre di krill"],
    ["un liquore", "la parte di un libro", "una fibra tessile", "una veste romana"],
    ["un grattacielo", "un ponte", "un lago", "un monte"]
    ]

risposte = [3,3,2]
punteggio = 0

for i, dom in enumerate(domande):
    print()
    print(dom)
    print(scelte[i])
    risposta = int(input("risposta (1-4)? "))
    if (risposta == risposte[i]):
        print("corretta!")
        punteggio += 1
    else:
        print("risposta sbagliata")
        
print("\nPunteggio: ", punteggio)
    