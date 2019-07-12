"""
Globais - Identificada em todo o programa
Locais - Identificada apenas no trecho em que foi declarada
"""


def teste():
    numero = 'Teste'
    print(numero)
    return numero


numero = 42
print(numero)
numero = teste()
