# file: miomodulo.py
#
# libreria personale

def saluta():
    print("ciao")

def saluta_nome(nome="Mario"):
    print(f"ciao, {nome}")
    
def somma(a, b):
    return a + b


if __name__ == "__main__":
    print("miomodulo dice: ", __name__)
    print("il modulo non è eseguibile")