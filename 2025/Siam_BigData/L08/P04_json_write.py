import json

doc = {"nome":"Mario Rossi", "cod":123, "data":"01012025",
       "materie" : [ {"cod": "python"}, {"cod": "math"}, {"cod": "eng"} ]}

with open("mydoc.json", "w") as f:
    json.dump(doc, f)