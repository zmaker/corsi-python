testo = []

while (True):
    cmd = input("> ")
    
    if cmd == 'q':
        print("grazie per aver usato ped")
        break
    elif cmd == 'h':
        print("h - help")
        print("q - esci")
        print("p - stampa")
        print("i - inserisci")
        print("x - elimina riga")
    elif cmd == 'i':
        line = input("line: ")
        testo.append(line)
    elif cmd == 'p':
        for i, l in enumerate(testo):
            print(f"{i} - {l}")
    elif cmd == 'x':
        x = int(input("che riga elimino? "))
        if (x >= 0) and (x < len(testo) ):
            testo.pop(x)