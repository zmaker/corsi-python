testo = []

print("[q] quit | [r] rm line | [h] help | [l] print | [s] save ")
while True:
    line = input(">")    
    if line == "q":
        break
    elif line == "r":
        d = int(input("che riga elimino?"))
        if (d >= 1) and (d <= len(testo)):
            testo.pop(d-1)
    elif line == "l":
        i = 1
        for el in testo:
            print(f"{i} {el}")
            i += 1
    elif line == "h":
        print("[q] quit | [r] rm line | [h] help | [s] save")
    elif line == "s":
        f = open("editor.txt", "w")
        for ll in testo:
            f.write(ll)
            f.write("\n")
        f.close()
    else:
        testo.append(line)
