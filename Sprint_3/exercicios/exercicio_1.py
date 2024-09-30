#Desenvolva um código em Python que crie variáveis para armazenar o nome e a idade de uma pessoa, 
# juntamente com seus valores correspondentes. 
# Como saída, imprima o ano em que a pessoa completará 100 anos de idade.

import datetime

nome = 'Luana'
idade = 25

ano_atual = datetime.datetime.now().year
anos = 100 - idade
ano_100_anos = ano_atual + anos

print(ano_100_anos)