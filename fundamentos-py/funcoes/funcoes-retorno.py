"""
numeros = [1, 2, 3]
ret_pop = numeros.pop()

print(ret_pop)

ret_print = print(numeros)
print(ret_pop)
----
def quadrado_de_7():
    return 7 * 7


def diz_oi():
    return "Oi, "


pessoa = "Rafael!"
print(diz_oi() + pessoa)
-----


def nova_funcao(variavel: None):
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    else:
        return 'B'


var1 = True
var2 = None
var3 = False

print(nova_funcao(var1))
print(nova_funcao(var2))
print(nova_funcao(var3))
----
def outra_funcao():
    return 1, 2, 3, 4

num1, num2, num3, num4 = outra_funcao()

print(num1, num2, num3, num4)
print(outra_funcao())
---------
from random import random
def joga_moeda():
    valor = random()
    if valor > 0.5:
        return "Cara"
    return "Coroa"


for i in range(1, 11):
    print(joga_moeda())
"""
def impar(numero):
    if numero % 2 != 0:
        return "Impar"
    return "Par"

for i in range(1,11):
    print(f'{i} é: {impar(i)}')





