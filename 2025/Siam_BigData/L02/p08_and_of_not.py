
piove = False
vento = True

if (piove or vento):
    print("resto a casa")
else:
    print("vado a fare la spesa")
    
if (piove and vento):
    print("pessima giornata")
else:
    print("è autunno")
    
if not piove:
    print("non piove")