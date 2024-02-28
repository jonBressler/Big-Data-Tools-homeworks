# JSON = JavaScript Object Notation

import json

# LOADING JSON DATA FROM A FILE
with open("data.json", "r") as f:
    data = json.load(f)

print(data.items())