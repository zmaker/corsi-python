a = "hello"
b = 'world'
c = a + " " + b + str(2)
print(c)

n = 12
tipo = "oro"
msg = "ho in tasca {} monete di {}"
print(msg.format(n, tipo))

msg = "nel mezzo del cammin"
print(msg[2])

if "zo" in msg:
    print("trovato")
    
print(msg[2:8])
print(msg[:8])
print(msg[7:])
print(msg[:-4])

msg = "  nel mezzo del cammin  "
print(msg)
print(msg.strip())
print(msg.upper())
print(msg.lower())
print(msg.replace("e", "*"))

parole = msg.strip().split(" ")
print(parole)

print(msg.index("del"))

    