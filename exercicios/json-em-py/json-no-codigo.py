import json

data = {
    "name":"wallace",
    "idade":21
}

json_data = json.dumps(data)

print(json_data)
