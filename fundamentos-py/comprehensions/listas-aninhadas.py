"""
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(listas)
print(listas[0])
print(listas[0][1])
print(listas[2])
print(listas[2][1])
print(listas[2][-2])

print("--------------")
# Iterando com loops:
for lista in listas:
    print(lista)
    for numero in lista:
        print(numero)

print("--------------")
# List Comprehension:
[[print(valor) for valor in lista] for lista in listas]
"""

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1,4)]for valor in range(1,4)]
print(velha)

# gerando valores iniciais
print(['*' for i in range(1,4) for i in range(1,4)])
