"""
numeros = {'a': 1, 'b': 2, 'c': 3,'d': 4,'e': 5}
quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
print(numeros)
print(quadrado)

numeros2 = [1, 2, 3, 4, 5, 1, 2]
quadrado2 = [valor ** 2 for valor in numeros2]
print(numeros2)
print(quadrado2)
------
chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]:valores[i] for i in range(0, len(chaves))}
print(mistura)
"""

# Logica condicional
numeros = [1, 2, 3, 4, 5]
res = {num:('par' if num % 2 == 0 else 'impar') for num in numeros}
print(res)



