try:
    f = open("readme.txt", "w")
    
except:
    print("errori")
finally:
    f.close()