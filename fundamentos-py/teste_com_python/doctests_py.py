"""
Doctests em Python: São testes que colocamos na docstring das funcoes/metodos Python.

Para todar um teste no doctest:
python -m doctest -v nomedomodulo.py

**********
def soma(a, b):
    Soma os numeros a e b
    >> > soma(1,2)
    3
    return a + b

print(soma(3, 4))
***********
# Outro exemplo aplicando o TDD

def duplicar(valores):
    Duplica os valores em uma lista
    #>>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]

    #>>> duplicar([])
    []

    #>>> duplicar(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    #>>> duplicar([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'

    return [2 * elemento for elemento in valores]
*************
# Erro inesperado
def fala_oi():
    Fala Oi
    #>>> fala_oi()
    'oi'
    # return "oi"  # retorna 'oi' e não "oi"
****************



"""


def verdade():
    """ Retorna verdade
    >>> verdade()
    True
    """
    return True


