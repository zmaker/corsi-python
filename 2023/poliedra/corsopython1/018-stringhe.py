a = "hello"
b = 'world'
c = a + ' ' + b
print(c)

n = 12
frutta = "mele"
msg = "Nel cesto ho {} {}"
print(msg.format(n, frutta))

msg = "nel mezzo del cammin"
print(msg[2])

n = len(msg)
print(f"lunghezza stringa {n}")

print("mezzo" in msg)
if ("del" in msg):
    print("trovato del")
    
print(msg[2:10])
print(msg[:10])
print(msg[12:])
print(msg[2:-2])

msg = "   Nel Mezzo Del Cammin  "
print(msg)
msg = msg.strip()
print(msg)

print(msg.upper())
print(msg.lower())

#key = input("parola da cercare? ")
#if key.upper() in msg.upper():
#    print("trovato");
    

print("e1", msg.replace("e", "*"))
print("e2", msg.replace("Del", "per"))

msg = "12 223 45 65 78 8"
lista = msg.split(" ")
for token in lista:
    print(token)

print("uso di index")
msg = "Nel Mezzo# Del Cammin"
n = msg.index("#")
print(n)
a = msg[:n]
b = msg[n+1:]
print(a)
print(b)

