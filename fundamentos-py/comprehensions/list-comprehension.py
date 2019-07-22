"""
Possivel gerar novas listas com dados processados a partir de outro iteravel

- Sintaxe:
[ dado for dado in interavel ]
--------
# for numero in numeros
# numero * 10
numeros = [1, 2, 3, 4, 5]
res = [numero * 10 for numero in numeros]
print(res)


def funcao(valor):
    return valor * 2


res = [funcao(numero) / 2 for numero in numeros]

print(res)
--------
numeros = [1, 2, 3, 4, 5]
numeros_dobrados = [valor * 2 for valor in numeros]
print(numeros_dobrados)

numeros_dobrados = []
for numero in numeros:
    numero_dobrado = numero * 2
    numeros_dobrados.append(numero_dobrado)

print(numeros_dobrados)
"""

nome = 'Rafael Alves'
print(nome)
print([letra.upper() for letra in nome])

amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']

def caixa_alta(nome):
    return nome.replace(nome[0], nome[0].upper())


print([caixa_alta(amigo) for amigo in amigos])
print([numero * 3 for numero in range(1, 10)])
print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])
