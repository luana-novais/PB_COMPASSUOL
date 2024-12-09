import random
import time
import os
import names

random.seed(40)

qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

aux = []
for i in range(0, qtd_nomes_unicos):
    aux.append(names.get_full_name())

print(f'Gerando {qtd_nomes_aleatorios} nomes aleatórios')

dados = []
for i in range(0, qtd_nomes_aleatorios):
    dados.append(random.choice(aux))

# Caminho do arquivo para salvar
caminho_arquivo = "/home/luana/PB_LUANA_NOVAIS/Sprint_8/exercicios/geração-massa-dados/nome_aleatorios.txt"


with open(caminho_arquivo, "w") as file:
    for nome in dados: 
        file.write(f"{nome}\n")

print(f"\nOs nomes aleatórios foram salvos no arquivo '{caminho_arquivo}'.")
