print("Bem vindo a loja FashionStyle")
nome = str(input("Digite seu nome: "))
valor = float(input("Digite o valor da sua compra: "))

if (valor >= 250 and valor < 500):
    desconto_10 = valor * 0.10
    valor_final_10 = valor - desconto_10 
    print(f"PARABÉNS {nome}. VOCÊ GANHOU 10% DE DESCONTO O VALOR DA SUA COMPRA É {valor_final_10:.2f}, MAS PODE GANHAR 30% SE SUA COMPRA FOR ACIMA DE R$500,00")

elif(valor > 500):
    desconto_30 = valor * 0.30
    valor_final_30 = valor - desconto_30 
    print(f"PARABÉNS {nome}. VOCÊ GANHOU SUPER DESCONTO DE 30%, O VALOR DA SUA COMPRA É: {valor_final_30:.2f}")

else:
    print(f"POXA {nome}, FALTA POUCO PARA VOCÊ GANHAR 10% DE DESCONTO EM SUA COMPRA")