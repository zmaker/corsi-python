testo = ""

print("digita q per finire")

while True:
    line = input(">")
    if line == "q":
        break
    testo += line + "\n"

print (testo)