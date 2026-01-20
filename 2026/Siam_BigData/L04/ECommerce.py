class Cliente:
    def __init__(self, nome, cod, email):
        self.nome = nome
        self.cod = cod
        self.email = email

    def __str__(self):
        return f"C: {self.cod} - {self.nome}"

class Prodotto:
    def __init__(self, nome, cod, prezzo):
        self.nome = nome
        self.cod = cod
        self.prezzo = prezzo
    
    def __str__(self):
        return f"P: {self.cod} - {self.nome} - {self.prezzo}"

class Carrello:
    def __init__(self, cliente):
        self.cliente = cliente
        self.prodotti = []
    
    def aggiungiProdotto(self, p):
        self.prodotti.append(p)
    
    def getTotale(self):
        tot = 0
        for p in self.prodotti:
            tot += p.prezzo
        return tot
    
    def __str__(self):
        txt = ""
        for p in self.prodotti:
            txt += str(p) + "\n"
        return txt

c1 = Cliente("Mario", 123, "mario.rossi@gmail.com")

p1 = Prodotto("Mela", 12, 0.98)
p2 = Prodotto("Pera", 13, 1.98)
p3 = Prodotto("Fragole", 14, 4.23)

k1 = Carrello(c1)
k1.aggiungiProdotto(p1)
k1.aggiungiProdotto(p3)

tot = k1.getTotale()
print(tot)

print(k1)