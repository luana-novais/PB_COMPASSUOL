#Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados. Utilize a lista a seguir para testar sua função.

#['abc', 'abc', 'abc', '123', 'abc', '123', '123']

def remove_duplicadas(lista):
  return list(set(lista))

lista = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
nova_lista = remove_duplicadas(lista)
print(nova_lista)