import json
with open("./data/geomatches/geomatches.json", "r") as read_file:
    data = json.load(read_file)
print(len(data))