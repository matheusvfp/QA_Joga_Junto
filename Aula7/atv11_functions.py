from faker import Faker
import pandas as pd
from typing import List, Dict

faker = Faker('pt_BR')

def gerar_persona() -> dict:
    data = {
        "Nome": faker.name(),
        "Idade": faker.random_int(min=18, max=80),
        "Cidade": faker.city()
    }
    return data

def gerar_personas_quantidade(number_of_personas: int) -> list[dict[str,int]]:
    return [gerar_persona() for _ in range (number_of_personas)]

def gerar_dataframe(number_of_personas: int) -> pd.DataFrame:
    df_lista_personas = pd.DataFrame(gerar_personas_quantidade(number_of_personas))
    return df_lista_personas

def salvar_em_csv(df: pd.DataFrame, nome_do_arquivo: str) -> None:
    df.to_csv(nome_do_arquivo, index=False)