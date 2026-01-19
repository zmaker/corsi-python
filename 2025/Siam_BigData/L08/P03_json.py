import json

with open('object-sample.json') as f:
    doc = json.load(f)
    #stampa tutto il file
    print(doc)
    print(" ")
    #seleziono delle parti
    print("id: ", doc["id"])
    print("nome: ", doc["name"])
    print(doc["topping"])
    print()
    print(doc["batters"])
    print()
    print(doc["batters"]["batter"])
    print()
    print(doc["batters"]["batter"][0])
    print()
    print(doc["batters"]["batter"][0]["type"])
    #stampo tutti i batter
    batters = doc["batters"]["batter"]
    for el in batters:
        print(el["id"], "-", el["type"])
    
    print("topping: ")
    topping = doc["topping"]
    for el in topping:
        print(el["id"], "-", el["type"])
    