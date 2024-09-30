#Calcule o valor mínimo, valor máximo, valor médio e a mediana da lista gerada na célula abaixo:

import random

random_list = random.sample(range(500), 50)

sorted_list = sorted(random_list)
list_length = len(sorted_list)
if list_length % 2 == 0:
  mediana = (sorted_list[list_length // 2 - 1] + sorted_list[list_length // 2]) / 2
else:
  mediana = sorted_list[list_length // 2]

media = sum(random_list) / len(random_list)

valor_minimo = min(random_list)

valor_maximo = max(random_list)

print(f'Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}')

