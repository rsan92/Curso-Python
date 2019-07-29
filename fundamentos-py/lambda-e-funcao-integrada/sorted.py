"""
Sorted
----
lista = [4, 7, 3, 8, 1, 2]
print(sorted(lista))
print(lista)
numeros = [6, 1, 8, 2]
print(sorted(numeros, reverse=True))
print(sorted(numeros, reverse=True))
----
usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "vou sair hoje"]},
    {"username": "gal", "tweets": []}
]

print(usuarios)

# Ordenando por username - ordem alfabética
print(sorted(usuarios, key=lambda usuario: usuario["username"]))

# Ordenando pelo numero de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))

"""

musicas = [
    {"titulo": "Musica 1", "tocou": 3}
    , {"titulo": "Musica 2", "tocou": 2}
    , {"titulo": "Musica 3", "tocou": 4}
    , {"titulo": "Musica 4", "tocou": 32}
    , {"titulo": "Musica 5", "tocou": 0}
]

# Menos tocada
print(sorted(musicas, key=lambda musica: musica["tocou"]))
# Mais tocada
print(sorted(musicas, key=lambda musica: musica["tocou"], reverse=True))
