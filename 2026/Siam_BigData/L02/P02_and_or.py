piove = False
giorno_mercato = True

if (piove and giorno_mercato):
    print("prendi l'ombrello")
    
nevica = True

if (nevica or piove):
    print("prendi cappello")
    
if not piove:
    print("giorno di sole")
    
temp = 8
if (temp < 20) and (temp >= 10):
    print ("t nella norma")
    
if (temp < 10) or (temp > 20):
    print("allarme temperatura")