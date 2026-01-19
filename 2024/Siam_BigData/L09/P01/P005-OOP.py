class Auto:
    def __init__(self, colore, anno):
        self.color = colore
        self.year = anno
        self.speed = 0

    def setSpeed(self, vel):
        self.speed = vel

    def beep(self, sound):
        return f"dice: {sound}"

class Fiaz500(Auto):
    def beep(self, sound="bip bip"):
        return f"500 says: {sound}"

    def doppietta(self):
        print("cambia in fretta")


class Perrari(Auto):
    def beep(self, sound="BOOOOP"):
        return f"Perrari says: {sound}"

a = Perrari("rossa", 1984)
b = Fiaz500("gialla", 1970)

print(a.beep())
print(b.beep())

