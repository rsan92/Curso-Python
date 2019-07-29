"""
Min e Max
----
max() -> Retorna o maior valor em um iteravel ou maior entre dois ou mais elementos
-
lista = [1, 8, 60, 4, 99, 129, 500, 3]
print(max(lista))

tupla = {1, 8, 60, 4, 99, 129, 500, 3}
print(max(tupla))

dicionario = {'a': 1, 'b': 8, 'c': 60, 'd': 99, 'e': 6}
print(max(dicionario.values()))
-
a = int(input("Informe o valor 1: "))
b = int(input("Informe o valor 2: "))
print(max(a, b))
print(max(1, 2, 3, 4))
print(max("Rafael"))
----
min() -> Retorna o menor item ou valor em um iteravel ou em dois ou mais elementos
-
lista = [1, 8, 60, 4, 99, 129, 500, 3]
print(min(lista))

tupla = {1, 8, 60, 4, 99, 129, 500, 3}
print(min(tupla))

dicionario = {'a': 1, 'b': 8, 'c': 60, 'd': 99, 'e': 6}
print(min(dicionario.values()))
-
nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']
print(max(nomes))  # Tim
print(min(nomes))  # Arya

print(max(nomes, key=lambda nome: len(nome)))  # Ollivander
print(min(nomes, key=lambda nome: len(nome)))  # Tim
"""
musicas = [
    {"titulo": "Musica 1", "tocou": 3}
    , {"titulo": "Musica 2", "tocou": 2}
    , {"titulo": "Musica 3", "tocou": 4}
    , {"titulo": "Musica 4", "tocou": 32}
    , {"titulo": "Musica 5", "tocou": 0}
]

print(max(musicas, key=lambda musica: musica["tocou"]))
print(min(musicas, key=lambda musica: musica["tocou"]))

print(max(musicas, key=lambda musica: musica["tocou"])["titulo"])
print(min(musicas, key=lambda musica: musica["tocou"])["titulo"])

