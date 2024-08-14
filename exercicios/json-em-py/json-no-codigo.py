import json

with open("dados.json", "r") as target:
    data = json.load(target)

print(data["nome"])
