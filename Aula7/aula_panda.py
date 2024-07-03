import pandas as pd

dados = {
    "Nome" : ["João", "Marta", "Ary", "Matheus","Lucas"],
    "Idade" : [51,37,23,24,45],
    "Cidade" : ["Recife", "Recife","Recife", "São Paulo", "Manaus"]
}

df = pd.DataFrame(data=dados)

print(df[df['Cidade'] == 'Recife'])


#for indice, linha in df.iterrows():
#   if linha['Cidade'] == 'Recife':
#       print(f"Nome: {linha['Nome']}, Idade: {linha['Idade']}, Cidade: {linha['Cidade']}")
