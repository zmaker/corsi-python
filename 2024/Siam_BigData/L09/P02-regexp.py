import re
if (re.match(r"^\S+@\S+\.\S+$", "info@tin.it") != None):
    print("match")
else:
    print("no match")