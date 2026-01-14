'''
a = 5
b = 7
c = 6
d = 7
media = (a+b+c+d) / 4
print(media)
'''

voti = []

n = int(input("voto: "))
voti.append(n)
n = int(input("voto: "))
voti.append(n)
n = int(input("voto: "))
voti.append(n)
n = int(input("voto: "))
voti.append(n)

media = (voti[0] + voti[1] + voti[2] + voti[3]) / 4
print(media)