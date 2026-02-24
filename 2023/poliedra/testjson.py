import json
data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)
    
str_con_json = json.dumps(data)
print(str_con_json)

str_con_json = json.dumps(data, indent=2)
print(str_con_json)

with open("data_file.json", "r") as read_file:
    data = json.load(read_file)
    
json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""
data = json.loads(json_string)
print(data["researcher"]["name"])
print(data["researcher"]["relatives"])
print(data["researcher"]["relatives"][0]["name"])