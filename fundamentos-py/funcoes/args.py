"""
def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3


print(soma_todos_numeros(1, 2, 3))
----
def soma_todos_numeros(nome, sobrenome, *args):
    return sum(args)
    total = 0
    for numeros in args:
        total += numeros
    return total


print(soma_todos_numeros('rafael','alves',1,2))
print(soma_todos_numeros('rafael','alves',1,2,3,4))
-----
def verifica_info(*args):
    if 'rafael' in args and 'alves' in args:
        return 'Bem-vindo Rafael'
    return 'Não sei quem é você'

print(verifica_info('rafael'))
print(verifica_info('alves'))
print(verifica_info('teste'))
print(verifica_info(True, 'alves', 'rafael', 333333))
"""


def soma_todos_numeros(*args):
    return sum(args)


print(soma_todos_numeros(3, 4, 5))
numeros = [1, 2, 3, 4, 5]
print(soma_todos_numeros(*numeros))  # *serve para informar que estamos enviando uma coleção para a função
# print(soma_todos_numeros(numeros))  # TypeError


