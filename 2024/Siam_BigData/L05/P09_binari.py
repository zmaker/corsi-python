file = open("bug.ico", "rb")
#print(file.read())

i = 0

n = file.read(1)
while (n):
    print(f"{i}. {n}")
    n = file.read(1)
    i += 1
    if (i == 10):
        break

file.close()

