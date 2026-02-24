testo = []

while True:
    print("[q] quit | [r] del line | [s] save | [l] load")
    
    line = input(">")

    if line == "q":
        break
    elif line == "r":
        d = int(input("che linea elimino?"))
        if (d >= 1) and (d <= len(testo)):
            testo.pop(d-1)
        else:
            print("riga non valida")
    elif line == "s":
        f = open("editor.txt", "w")
        for ll in testo:
            f.write(ll)
            f.write('\n')
        f.close()
    elif line == "l":
        #lettura file
    else:
        testo.append(line)
    
    i = 1
    for el in testo:
        print(f"{i}: {el}")
        i += 1
        

print (testo)