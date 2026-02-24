testo = ""

print("premi q per terminare")
while True:
    line = input(">")    
    if line == "q":
        break
    else:
        testo += line + "\n";
print(testo)