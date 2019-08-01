"""
def quadrado(numero):
    return numero ** 2

def cubo(numero):
    return numero ** 3

def elevar(numero, elevado):
    return numero ** elevado

def somar (a, b):
    return a + b

def multiplicar (a, b):
    return a * b

def outra(num1, b, msg):
    return (num1 + b) * msg


print(somar(2, 5))
print(somar(10, 20))
print(multiplicar(4, 5))
print(multiplicar(2, 8))
print(outra(3, 2, 'Python '))
print(outra(5, 4, 'Python '))
--------
def nome_completo(nome, sobrenome):
    return f'Seu nome completo é: {nome} {sobrenome}'


nome = 'Rafael'
sobrenome = 'Alves'
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome=sobrenome, nome=nome))
"""
def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total += num
    return total


lista = [1, 2, 3, 4, 5, 6, 7]
# print(soma_impares(lista))

# lista = {1, 2, 3, 4, 5, 6, 7}

# print(soma_impares(lista))
