with open('number.txt') as file:
    numeros = file.readlines()
    
    numeros = list(map(int, numeros))
    pares = list(filter(lambda x: x % 2 == 0, numeros))
    ordenar = sorted(pares, reverse = True)
    cinco_maiores = ordenar[:5]
    soma = sum(cinco_maiores)
    print(cinco_maiores)
    print(soma)