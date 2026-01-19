import random

max_val = 0

ans = 's'
while (ans == 's'):
    # estraggo un numero a caso
    n = random.randint(0,99)
    
    print(n)
    
    if (n > max_val):
        max_val = n
        
    print("il valore massimo fino ad ora:", max_val)

    #eseguo di nuovo?
    ans = input("Altro numero? (s/n) ")

print("il valore massimo è:", max_val)