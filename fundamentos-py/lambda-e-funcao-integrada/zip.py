"""
Cria um iteravel (Zip Object) que agrega elemento de cada um dos iteraveis passados como entrada em pases
"""

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [7, 8, 9]
zip1 = zip(lista1, lista2)

print(zip1)
print(type(zip1))

print(list(zip(lista1, lista2)))
print(tuple(zip(lista1, lista2)))
print(set(zip(lista1, lista2)))

zip1 = zip(lista1, lista2, lista3)
print(list(zip1))