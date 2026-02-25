import random

risposta = 's'
while risposta == 's':
    #estraggo numeri
    n = random.randint(1,91)
    print(n)
    #chiedo se ne serve un'altro
    risposta = input("estraggo un nuovo numero (s/n)? ")
    
print("END")