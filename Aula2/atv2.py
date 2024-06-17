nome = input("Digite seu nome: ")
soma_notas = 0

for i in range(4):
    nota = float(input(f"Digite a nota {i+1}: "))
    soma_notas += nota

media = soma_notas / 4
print(f"Olá, {nome}! Sua média é: {media} pontos")
