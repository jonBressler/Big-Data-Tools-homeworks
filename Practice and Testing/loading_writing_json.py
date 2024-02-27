# JSON = JavaScript Object Notation

import json

# LOADING JSON DATA FROM A FILE
with open("data.json", "r") as f:
    data = json.load(f)

print(data.items())


# WRITING JSON DATA TO A FILE
# open the json in "write" mode

# with open("data2.json", "w") as f:
#     json.dump(data, f)