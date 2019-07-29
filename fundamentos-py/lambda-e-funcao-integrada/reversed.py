"""
Reversed() -> Funciona com qualquer iteravel

"""

lista = [1, 2, 3, 4, 5]
res = reversed(lista)
print(res)
print(list(reversed(lista)))
print(tuple(reversed(lista)))
print(set(reversed(lista)))  # Set não guarda a ordem, por isso o reverse não tem efeito

print("---")
for letra in reversed('Rafael Sousa Alves Nobre'):
    print(letra, end='')
print()
print(''.join(list(reversed('Rafael Sousa Alves Nobre'))))
print()
for n in reversed(range(0, 10)):
    print(n)
for n in range(9, -1, -1):
    print(n)


