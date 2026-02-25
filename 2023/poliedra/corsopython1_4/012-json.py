import json
data = {"nome":"Mario", "cognome":"Rossi"}

with open("data1.json", "w") as jf:
    json.dump(data, jf)

jstr = json.dumps(data)
print(jstr)

jstr = json.dumps(data, indent=2)
print(jstr)

with open("data1.json", "r") as jf:
    pers = json.load(jf)
    print(pers["nome"])
    print(pers["cognome"])
    
jstr =  """
{
    "nome":"Mario",
    "cognome":"Rossi",
    "anno":1989,
    "hobby":["bici", "musica", "pittura"],
    "figli":[
        {"nome":"Anna", "anno":2000},
        {"nome":"Marco", "anno":2005}
        ]
}
"""
data = json.loads(jstr)
print(data["nome"])
print(data["hobby"][0])
print(data["hobby"][1])
print(data["figli"][0]["nome"])

