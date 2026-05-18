print("Adventure game\n")
print("Sei in una foresta magica e il sole sta tramontando.")
print("Da che parte vuoi andare?")

mossa = input("n, s, w, e? ")

if (mossa == 'n'):
    print("sei uscito dalla foresta")
elif (mossa == 's'):
    print("la foresta ti circonda sempre più'")
elif (mossa == 'e'):
    print("appare una capanna in una radura")
elif (mossa == 'w'):
    print("un feroce Wumpus ti assale")
else:
    print("comando non valido")
    