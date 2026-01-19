def stampaPersone(*persone):
    #...
    print("numero di parametri:", len(persone))
    for p in persone:
        print(p, end=" ")
    print("")
    
stampaPersone("mario")
stampaPersone("mario", "luigi", "anna")

def assettoDrone(pitch, roll, yaw):
    print(f"p: {pitch}, r:{roll}, y: {yaw}")
    
assettoDrone(12,0,90)
assettoDrone(yaw=90, roll=23, pitch=56)

def assettoDrone2(pitch=90, roll=0, yaw=180):
    print(f"p: {pitch}, r:{roll}, y: {yaw}")

assettoDrone2(yaw=90)