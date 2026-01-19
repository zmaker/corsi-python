# gioco "il milionario" o "quiz patente"
# propone x domande, attende una risposta tra 4 possibili
# calcola il punteggio totale

punteggio = 0

domande = ["Cos'è un abacà?",
           "Qual è la risposta universale?",
           "Qual è il 6 pianeta del sistema solare?"]
alternative = [['liquore', 'libro', 'fibra tessile', 'veste romana'],
               ['non so','tutto','42','0'],
               ['giove','marte','terra','saturno']]

risposte = [2,2,3]

for i in range(3):
    # propone una domanda con 4 risposte
    print(domande[i])
    #stampa alternative
    for alternativa in alternative[i]:
        print("\t", alternativa)
    # attende risposta (a,b,c,d)
    ans = input("che risposta dai (0,1,2,3)? ")
    risp = int(ans)
    #verifico risposta
    if risp == risposte[i]:
        # se risposta corretta aumento punteggio
        print("Corretto!")
        punteggio += 1
    else:
        print("Sbagliato!")
    
# alla fine del gioco stampo il punteggio totale
print(f"Il tuo punteggio: {punteggio}")