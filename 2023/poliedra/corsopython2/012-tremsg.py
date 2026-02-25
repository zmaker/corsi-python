messaggi = []

num_cose = int(input("quante cose ti servono? "))

for i in range(num_cose):
    ans = input("il tuo messaggio: ")
    messaggi.append(ans)

input("premi invio per vedere i messaggi")
for i in range(num_cose):
    print(f"{i+1}: item-> {messaggi[i]}")