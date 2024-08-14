import json

data = {
    "nome": "João",
    "idade": 30,
    "email": "joao@email.com"
}

json_data = json.dumps(data)

with open("novos_dados.json", "w") as file:
    file.write(json_data)
