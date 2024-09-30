# Escreva um código Python para imprimir os números pares de 0 até 20 (incluso).

numeros = list(range(0, 21))  

for numero in numeros:
  if numero % 2 == 0:
    print(f"{numero}")