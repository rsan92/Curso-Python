"""
Cria um iteravel (Zip Object) que agrega elemento de cada um dos iteraveis passados como entrada em pases
-----
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [7, 8, 9, 10, 11]
zip1 = zip(lista1, lista2)

print(zip1)
print(type(zip1))

print(list(zip(lista1, lista2)))
print(tuple(zip(lista1, lista2)))
print(set(zip(lista1, lista2)))

zip1 = zip(lista1, lista2, lista3)
print(list(zip1))
---
tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dicionario = {"a": 11, "b": 12, "c": 13, "d": 14, "e": 15}

zt = zip(tupla, lista, dicionario.values())
print(list(zt))

dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(list(zip(dados)))
print(list(zip(*dados)))
"""
prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(list(zip(alunos, prova1, prova2)))

print(final)

