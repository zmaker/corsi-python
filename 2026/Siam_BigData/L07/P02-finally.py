try:
    f = open("readme.txt", "w")

except:
    print("errore file")

finally:
    f.close()

with open("file.txt", "r" ) as f:
    f.read()