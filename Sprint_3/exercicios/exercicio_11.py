#Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.

import json

arquivo = open("person.json", "r")
dados = json.load(arquivo)
arquivo.close()

print(dados)