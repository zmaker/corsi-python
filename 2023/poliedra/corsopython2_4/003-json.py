import json

jstr = """
{
    "nome":"mario",
    "cognome":"rossi",
    "anno":1998,
    "hobby":["chitarra", "cucina", "funky"],
    "figli":[
            {"nome":"Anna", "anno":"2010"},            
            {"nome":"Marco", "anno":"2012"}
        ]
}
"""
#print(jstr)
data = json.loads(jstr)
#print(data)
print(data["nome"])
print(data["cognome"])
print(data["hobby"][0])
print(data["hobby"][1])
print(data["figli"][0]["nome"])

with open("mario.json", "r") as jf:
    data = json.load(jf)
    print("f:", data["nome"])
