import json

with open("dados.json", "r") as file:
    data = json.load(file)

data["nome"] = "wallace barros"

with open("dados.json", "w") as file:
    json.dump(data, file)
