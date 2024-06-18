nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if (idade == 18):
    print(f"{nome} possui idade mínima para dirigir")
elif (idade >= 17 and idade < 18):
    print(f"{nome} tem entre 17 e 18 anos e ainda NÃO está apto para dirigir")
else:
    print(f"{nome} NÃO possui idade mínima para dirigir")