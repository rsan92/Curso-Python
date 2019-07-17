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
encontre = 2
if encontre in lista1:
    print(f'Encontrei o {encontre}')
else:
    print(f'Não encontrei o {encontre}')
-------
encontre = "e"
if encontre in lista2:
    print(f'Encontrei o {encontre}')
else:
    print(f'Não encontrei o {encontre}')
-------
print(lista1)
lista1.sort()
print(lista1)
------
print(lista1.count(1))
print(lista2.count('e'))
------
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
lista6 = lista1 + lista4
print(lista6)
lista6.sort()
print(lista6)
lista6.reverse()
print(lista6)
--------
lista6 = lista1.copy()
print(lista6)
excluido = lista6.pop(0)
lista6.insert(0, 10)
print(lista6)
print(excluido)
lista6.clear()
print(lista6)
---------
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
soma = ''
for elemento in lista2:
    soma += elemento
    print(elemento)

print(soma)
--------
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
cores = ['verde', 'amarelo', 'vermelho']0000
print(cores[-1])
print(cores[0])
print(cores[-2])
-------------
Exemplo14
cores = ['verde', 'amarelo', 'azul', 'branco']

for indice, cor in enumerate(cores):
    print(indice, cor)
--------------
lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(33)

print(lista)
------------
lista = []
for n in range(1, 100):
    lista.append(f"numero{n}")

print(lista.index("numero11", 10))
--------------
# lista[inicio:fim:passo]
lista = [1, 2, 3, 4]
# print(lista[1:])
print(lista[2::-1])
--------------
nomes = ['Testando', 'Testes']
print(nomes)
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

nomes = ['Testando', 'Testes']
nomes.reverse()
print(nomes)
----------
lista = [1, 2, 3]
print(lista)

tupla = tuple(lista)
print(tupla)

num1, num2, num3 = lista
print(num1)
print(num2)
print(num3)
"""

lista = [1, 2, 3]
print(lista)

nova = lista.copy()
print(nova)

nova.append(4)

print(nova)
print(lista)

print("============")

lista = [1, 2, 3]
nova = lista
print(lista)
print(nova)

nova.append(4)
print(lista)
print(nova)

