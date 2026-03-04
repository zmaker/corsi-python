domande = [
    "Quale di queste affermazioni sulla balena è sbagliata?",
    "Che cos'è l'abacà",
    "Se a San Francisco vedo il Golden Gate, cosa sto osservando?"]

scelte = [
    ["ha i fanoni", "è un cetaceo", "ha 2 figli per volta", "si nutre di krill"],
    ["un liquore", "la parte di un libro", "una fibra tessile", "una veste romana"],
    ["un grattacielo", "un ponte", "un lago", "un monte"]
    ]

risposte = [3, 3, 2]

punteggio = 0

indice_domanda = 0
for dom in domande:
    print(dom)
    # stampo le possibili scelte
    print(scelte[indice_domanda])
    # attendere la risposta
    ans = int( input("cosa rispondi (1,2,3 o 4)? ") )
    
    # verifichero se la risposta è corretta
    if (ans == risposte[indice_domanda]):
        punteggio += 1
        print("risposta corretta!")
    else:
        print("sbagliato")
        
    #stampo una linea vuota
    print("")
    indice_domanda += 1

print("punti: ", punteggio)