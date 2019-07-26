"""
Sorted
----
lista = [4, 7, 3, 8, 1, 2]
print(sorted(lista))
print(lista)
numeros = [6, 1, 8, 2]
print(sorted(numeros, reverse=True))
print(sorted(numeros, reverse=True))

"""

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "vou sair hoje"]},
    {"username": "gal", "tweets": []}
]

print(usuarios)
print(sorted(usuarios, key=lambda usuario: usuario["username"]))
