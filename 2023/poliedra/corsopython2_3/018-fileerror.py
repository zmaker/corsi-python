try:
    f = open("readme.txt", "w")
    #scrivo...
except:
    print("file error")
finally:
    f.close()
    
with open("readme.txt", "w") as file:
    file.write("hello")