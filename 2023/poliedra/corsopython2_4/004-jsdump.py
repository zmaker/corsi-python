import json

with open("mario.json", "r") as jf:
    data = json.load(jf)
    
data["nome"] = "piero"

with open("piero.json", "w") as jf:
    json.dump(data, jf)
    
jstr = json.dumps(data)
print(jstr)

jstr = json.dumps(data, indent=2)
print(jstr)
