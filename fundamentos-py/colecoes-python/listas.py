"""
- Funcionam como vetores/matrizes/Arrays
- Sao dinamicos e podem conter QUALQUER tipo de dados
-------
lista1 = [100, 1, 4, 40, 22, 55, 0, 1, 1, 1, 1]
lista2 = ['t', 'e', 's', 't', 'e', 's', ' ', 't', 'e', 's', 't', 'a', 'n', 'd', 'o']
lista3 = []
lista4 = list(range(11))
lista5 = list('Testes Testando')
-------
Exemplo1:
encontre = 2
if encontre in lista1:
    print(f'Encontrei o {encontre}')
else:
    print(f'Não encontrei o {encontre}')
-------
Exemplo2:
encontre = "e"
if encontre in lista2:
    print(f'Encontrei o {encontre}')
else:
    print(f'Não encontrei o {encontre}')
-------
Exemplo3:
print(lista1)
lista1.sort()
print(lista1)
------
Exemplo4
print(lista1.count(1))
print(lista2.count('e'))
------
exemplo5
print(lista1)
lista1.append(1)
lista1.append(5)
lista1.append(16)
lista1.append([1, 5, 16])  # Coloca a lista como elemento unico
lista1.extend([1, 5, 16])  # Coloca cada elemento da lista como valor adicional na lista
lista1.extend('testes testando')
lista1.insert(0, 101)
print(lista1)
------
Exemplo7
lista6 = lista1 + lista4
print(lista6)
lista6.sort()
print(lista6)
lista6.reverse()
print(lista6)
--------
Exemplo8
lista6 = lista1.copy()
print(lista6)
excluido = lista6.pop(0)
lista6.insert(0, 10)
print(lista6)
print(excluido)
lista6.clear()
print(lista6)
---------
Exemplo9
curso = "Programação em Python"
print(curso)
curso = curso.split()
print(curso)

curso2 = "Programação,em,Python"
print(curso2)
curso2 = curso2.split(',')
print(curso2)

print(lista6)
curso3 = ' '.join(lista6)
print(curso3)

curso4 = '$'.join(lista6)
print(curso4)
-------
Exemplo10
soma = ''
for elemento in lista2:
    soma += elemento
    print(elemento)

print(soma)
--------
Exemplo11
carrinho = []
produto = ''
while produto != 'sair':
    print('Adicione um produto na lista ou digite "sair"')
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)
----------
Exemplo12
numeros = [1, 2, 3, 4, 5]
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros2 = [num1, num2, num3, num4, num5]

print(numeros)
print(numeros2)
------------
Exemplo13
cores = ['verde', 'amarelo', 'vermelho']
print(cores[-1])
print(cores[0])
print(cores[-2])
"""

cores = ['verde', 'amarelo', 'azul', 'branco']

for indice, cor in enumerate(cores):
    print(indice, cor)

