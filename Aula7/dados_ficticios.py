import pandas as pd


dados = pd.read_csv('C:/Users/Matheus/Desktop/QA Joga Junto/Python/Aula7/dados_ficticios.csv')

df = pd.DataFrame(dados)

df_renda = (df[df['renda'] > 5000])
df_idade = (df[df['idade'] > 40])
df_idade_renda = (df[(df['idade'] > 40) & (df['renda'] > 5000)])

print(df_idade_renda)

