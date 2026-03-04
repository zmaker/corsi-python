import random

while (True):
    input("premi invio per lanciare un dado ")
    n = random.randint(1, 6)
    print(n)
    
    ans = input("ancora (s/n)? ")
    if (ans != 's'):
        break
        
