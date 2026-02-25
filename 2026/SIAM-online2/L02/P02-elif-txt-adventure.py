print("Sei in una foresta magica e il sole sta tramontando.")
print("Da che parte vuoi andare?")

move = input("n, s, w, e? ")

if (move == 'n'):
    print("sei uscito dalla foresta")
elif (move == 's'):
    print("la foresta ti circonda ancora")
elif (move == 'e'):
    print("Appare una capanna in una radura")
elif (move == 'w'):
    print("Un feroce Wumpus ti assale")
else:
    print("??")
