"""
len() -> Retorna o tamanho de um iteravel
print(len('Rafael'))
# Dunder len é chamada quando chamamos o len()
print("rafael".__len__())

print(len([1, 2, 3, 4]))
print(len({1, 2, 3, 4}))
print(len((1, 2, 3, 4)))
print(len({"a": 1, "b": 2, "c": 3}))
---
abs() -> Retorna o valor absoluto de um numero inteiro ou real
print(abs(-5))  # 5
print(abs(5))  # 5
print(abs(3.14))  # 3.14
print(abs(-3.14))  # 3.14
---
sum() -> Recebe como parametro um iteravel e retorna a soma total dos elementos.
print(sum([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5], 50))  # valor inicial = 50

print(sum({1, 2, 3, 4, 5}))
print(sum((1, 2, 3, 4, 5)))
print(sum({"a":1, "b":2, "c":3, "d":4, "e":5}.values()))
---
round() -> retorna um numero arredondado para N digitos de precisão
"""
print(round(10.2))
print(round(10.5))
print(round(10.6))
print(round(1.21212121, 2))
print(round(1.21999999, 2))












