
RUN = True

while (RUN):
    print("hello !")
    
    #chiedo all'utente se vuole continuare
    ans = input("ancora? (s/n) ")
    if ans != 's':
        RUN = False

print("bye!")