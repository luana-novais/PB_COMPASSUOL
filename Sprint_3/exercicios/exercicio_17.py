#Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas: a lista recebida dividida em 3 partes iguais. Teste sua implementação com a lista abaixo

#lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def dividir_lista(lista):
  
    tamanho = len(lista)
    terco = tamanho // 3
    lista1 = lista[:terco]
    lista2 = lista[terco:2 * terco]
    lista3 = lista[2 * terco:]
    return lista1, lista2, lista3

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
lista1, lista2, lista3 = dividir_lista(lista)
print(lista1, lista2, lista3)
