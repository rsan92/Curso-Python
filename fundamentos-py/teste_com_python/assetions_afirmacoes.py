"""
Assertions (Checagens/Questionamentos)

Utilizamos o 'assert' em uma expressão que queremos checar se é válida ou não
Se for verdadeira, o assert retorna None.
Se for falsa, levanta um erro do tipo AssertionError.
# OBS: É possível definir um argumento ou msg de erro personalizada
"""


def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos número precisam ser positivos'
    return a + b


ret = soma_numeros_positivos(2, 4)  # 6
# ret = soma_numeros_positivos(-2, 4)  # AssertionError
print(ret)


def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'doces'
    ], 'A comida precisa ser fast food'
    return f'Eu estou comendo {comida}'


# ret = comer_fast_food('salada')  # AssertionError: A comida precisa ser fast food
ret = comer_fast_food('pizza')  # Eu estou comendo pizza
print(ret)


# CUIDADO ao utilizar assert
# Se o pgm python for executado com o parametro -O, nenhum assertion será validado.








