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
        print("o - open file")
        print("w - write file")
        print("n - new buffer")
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
            
    elif cmd == 'n':
        #nuovo buffer
        testo = []
        
    elif cmd == 'o':
        #apre il file
        f = open("doc1.txt")
        testo = []
        for l in f:
            testo.append(l[:-1])
        f.close()
        
    elif cmd == 'w':
        #scrive file
        f = open("doc1.txt", "w")
        for l in testo:
            f.write(l)
            f.write("\n")
        f.close()
