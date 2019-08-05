"""
Funcoes de Maior Grandeza - Higher Order Functions - HOF
------------
def somar(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def dividir(a, b):
    return a / b


def multiplicar(a, b):
    return a * b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


print(calcular(4, 3, somar))
print(calcular(4, 3, diminuir))
print(calcular(4, 3, multiplicar))
print(calcular(4, 3, dividir))
==========
# Nested Functions - Funcoes Aninhadas
# É possível ter funcoes dentro de funcoes. (inner functions / nested functions

from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(['E aí', 'Suma Daqui', 'Gosto muito de você'])
    return humor()+', '+pessoa


print(cumprimento('Rafael'))
print(cumprimento('Rafael'))
=========================
# Retornando funcoes de outras funcoes
from random import choice

def faz_me_rir():
    def rir():
        return choice(['hahahaha', 'kkkkkkk', 'hehehehe'])
    return rir


rindo = faz_me_rir()
print(rindo())
"""


# Inner functions podem acessar o escopo de funcoes externas ou mais externas.
from random import choice


def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(['hahaha', 'hehehehe', 'kkkkk'])
        return f'{risada} {pessoa}'
    return dando_risada


rindo = faz_me_rir_novamente('Rafael')
print(rindo())
print(rindo())
print(rindo())







