import atv11_functions as func

quant_personas = int(input("Digite a quantidade de personas: "))

df_lista_personas = func.gerar_dataframe(quant_personas)


print(df_lista_personas)