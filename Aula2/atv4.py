
tupla = ('hamburguer', 'Pizza', 'Feijoada', 'Lasanha', 'Sorvete')

lista = list(tupla)

lista.extend(['Biscoito', 'Frango']) 

lista.pop(0)

lista.pop()

print(f"primeiro dado da lista: {lista[0]}")

print(f"Quantidade de dados na lista: {len(lista)}")

dicionario = {
    "nome": "Lucas",
    "idade": 35,
    "profissão": 'QA'
}

print(dicionario['nome'])