import time
import random

t = 0
h = 0
l = 0

thluce = 50
thhum = 20
thtemp = 15

WATER = False
LIGHT = False
HEAT = False

while True:
    #misuro temp
    t = random.randint(0, 60)
    #misuro humidita
    h = random.randint(0, 100)
    #misuro luce
    l = random.randint(0, 100)
    
    print(f"t: {t}\th: {h}\t luce:{l}")
    
    #calcolo attivazioni
    if (t > thtemp) and (h < thhum) and (l < thluce):
        WATER = True
    elif (t > thtemp) and (h < thhum) and (l > thluce):
        WATER = True
    
    if (t < thtemp) and (h < thhum) and (l > thluce):
        LIGHT = True
    elif (t > thtemp) and (h > thhum) and (l < thluce):
        LIGHT = True
        
    if (t < thtemp):
        HEAT = True

    #applico le uscite/attivazioni
    if (WATER):
        print("WATER")
    if (LIGHT):
        print("LIGHT")
    if (HEAT):
        print("HEAT")
        
    time.sleep(1)