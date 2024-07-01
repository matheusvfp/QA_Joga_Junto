import requests

cep = input("qual o seu cep: ")

responde = requests.get(f"https://viacep.com.br/ws/{cep}/json/")

print(f"O Status code é:{responde.status_code}")

data = responde.json()

print(f"O logradouro da chamda é: {data['logradouro']}")
