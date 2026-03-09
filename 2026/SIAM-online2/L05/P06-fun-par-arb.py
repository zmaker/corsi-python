# parametri arbitrari

def cugini(*c):
    print(len(c))
    for cugino in c:
        print(cugino, end=" ")
    print("")

cugini()
cugini("luigi")
cugini("luigi", "mario", "anna")