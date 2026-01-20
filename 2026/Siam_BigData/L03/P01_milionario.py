domande = [
    'Quale di queste affermazioni sulla balena è sbagliata?',
    "che cos'è l'abacà?",
    "se siete a San Francisco e vedete il Golden Gate, " \
    "cosa state osservando?"
    ]
scelte = [
    ['ha i fanoni', 'è un cetaceo', 'ha 2 figli per volta', 'si nutre di krill'],
    ['un liquore','la parte di un libro','una fibra tessile','una veste romana'],
    ['grattacielo','ponte','lago','monte']
    ]
risposte = [3,3,2]

'''
strutture dati alternative - da provare
domande = [
    "domanda1", "ris1", "ris2", "ris3", "ris4", 2,
    "domanda2", "ris1", "ris2", "ris3", "ris4", 2,
    
    ]

domande = [
    ["domanda1", ["ris1", "ris2", "ris3", "ris4"], 2],
    ["domanda2", ["ris1", "ris2", "ris3", "ris4"], 2],
    
    ]

print(domande[0])
print(domande[0][0])
print(domande[0][1])
print(domande[0][2])

print(domande[0][1][1])

domanda = domande[0]
print(domanda)
testo = domanda[0]
print(testo)
risposte = domanda[1]
print(risposte)
ris_corretta = domanda[2]
print(ris_corretta)

'''

#indice domanda corrente
idom = 0

#punteggio
punti = 0

for dom in domande:
    # stampo la domanda
    print(dom)
    # stampo LE POSSIBILI scelte
    c = 1
    for cho in scelte[idom]:
        print(f"\t{c}: {cho}")
        c += 1
    
    #attendo la risposta
    ans = int(input("cosa scegli? (1,2,3,4) "))
    
    #verifico la risposta
    risposta_corretta = risposte[idom]
    if (ans == risposta_corretta):
        print(":-)")
        punti += 1
    else:
        print(":-(")
    
    #incremento l'indice della domanda corrente
    idom += 1
    
    #inserisco una riga vuota 
    print("")
    
print(f"Hai indovinato {punti} domande su {len(domande)}")