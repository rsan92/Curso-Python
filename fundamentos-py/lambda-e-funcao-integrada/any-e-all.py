"""
Any e All
------
all()-> Retorna True se todos os elementos do iteravel são verdadeiros ou está vazio
print(all([0, 1, 2, 3, 4]))  # Todos os numeros são verdadeiros? False, pois 0 é false
print(all([1, 2, 3, 4]))  # True
print(all([]))  # True
print(all((1, 2, 3)))  # True
print(all({1, 2, 3}))  # True
print(all("Teste"))  # True
----
nomes = ["Carlos", "Camila", "Carla", "Cassiano", "Cristina"]
print(all(nome[0] == "C" for nome in nomes))  # todos os nomes iniciam com "C"
print(all(letra for letra in 'eio' if letra in 'aeiou'))

print(all(num for num in [4, 2, 10, 6, 8] if num%2 == 0))
----
any()-> Retorna True se qualquer elemento for verdadeiro. Retorna False se estiver vazio
"""
print(any([0, 1, 2]))  # True
print(any([0, 0]))  # False




