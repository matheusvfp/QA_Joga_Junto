def verificar_paridade(matricula):
    numero = int(matricula)
    
    if numero % 2 == 0:
        return 'VOCÊ ESTÁ NO TIME AZUL'  
    else:
        return 'VOCÊ ESTÁ NO TIME AMARELO'  
    
matricula = int(input("digite o numero de matricula: "))

print(verificar_paridade(matricula))