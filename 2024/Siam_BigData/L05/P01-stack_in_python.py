# programma post-it in python
#
# inserisco una nota dopo l'altra
# leggo l'ultima (pop)
# quando leggo una nota, la elimino dallo stack
# posso stampare tutte le note

# creo una struttura per memorizzare i dati - es una lista
pila = []

# il programma è interattivo
while (True):
    #cosa vuoi fare?
    cmd = input("? ")
    if (cmd == 'q'):
        print("bye")
        break
    elif (cmd == 'i'):
        #aggiungo una nota
        nota = input("nota: ")
        pila.append(nota)
    elif (cmd == 'l'):
        i = 1
        for el in pila:
            print(f"{i}: {el}")
            i += 1
            
    elif (cmd == 'p'):
        #assert len(pila) > 0
        if len(pila) > 0:
            el = pila.pop()
            print(el)
        else:
            print("pila vuota")
    else:
        print("???")
    
print("programma concluso")