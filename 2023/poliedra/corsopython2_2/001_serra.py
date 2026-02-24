import time
import random

t = 0
h = 0
l = 0

thluce = 50
thhumi = 60
thtemp = 20

WATER = False
LIGHT = False
HEAT = False

while True:
    #misuro t
    t = random.randint(0, 40)
    #misuro h
    h = random.randint(0, 100)    
    #misuro l
    l = random.randint(0, 100)
    print(f"t: {t} h: {h} l: {l}")
    
    #elaboro
    if (t > thtemp) and (h < thhumi) and (l < thluce):
        WATER = True
    elif (t > thtemp) and (h > thhumi) and (l < thluce):
        WATER = True

    if ((t > thtemp) and (h < thhumi) and (l < thluce)) or \
       ((t > thtemp) and (h < thhumi) and (l > thluce)):
        LIGHT = True

    if (t < thtemp):
        HEAT = True

    #attivo
    if (WATER):
        print("WATER")
    if (HEAT):
        print("HEAT")
    if (LIGHT):
        print("LIGHT")
    
    time.sleep(1)