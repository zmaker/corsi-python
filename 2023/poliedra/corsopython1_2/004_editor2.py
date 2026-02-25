testo = []

while True:
    print("[q] quit | [r] del line")
    
    line = input(">")

    if line == "q":
        break
    elif line == "r":
        d = int(input("che linea elimino?"))
        if (d >= 1) and (d <= len(testo)):
            testo.pop(d-1)
        else:
            print("riga non valida")
    else:
        testo.append(line)
    
    i = 1
    for el in testo:
        print(f"{i}: {el}")
        i += 1
        

print (testo)