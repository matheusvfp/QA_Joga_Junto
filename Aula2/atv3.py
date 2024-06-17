import math
valor = float(input("Digite um valor: "))

dobro = valor * 2
print(f"O dobro de {valor} é: {dobro}")

triplo = valor * 3
print(f"O triplo de {valor} é: {triplo}")

quadrado = valor ** 2
print(f"O quadrado de {valor} é: {quadrado}")

raiz_quadrada = math.sqrt(valor)
print(f"A raiz quadrada de {valor} é: {raiz_quadrada:.4f}")

raiz_cubica = valor ** (1/3)
print(f"A raiz cúbica de {valor} é: {raiz_cubica:.4f}")