#Escreva uma função que recebe uma string de números separados por vírgula e retorne a soma de todos eles. Depois imprima a soma dos valores.

#A string deve ter valor  "1,3,4,6,10,76"

def soma_numeros(string_numeros):
    lista_num = string_numeros.split(',')
    numeros = [int(numero) for numero in lista_num]
    total = sum(numeros)
    
    return total

string_de_numeros = ("1,3,4,6,10,76")
resultado = soma_numeros(string_de_numeros)
print(resultado)  
