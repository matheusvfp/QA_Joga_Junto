from faker import Faker

faker = Faker('pt_BR')

def gerar_pessoa ():
    nome = faker.name()
    idade = faker.random_int(min=18, max=18)
    cidade = faker.city
    
    return{
        "Nome" : nome,
        "Idade" : idade,
        "Cidade" : cidade
    }
    
print(gerar_pessoa())