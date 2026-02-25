messaggi = []
for i in range(0,3):
    m = input("msg? ")
    messaggi.append(m)

print("ho n. ", len(messaggi), " messaggi.")
print(messaggi)

for m in messaggi:
    print(m)
    
for i in range(0, 3):
    print(str(i+1), messaggi[i])