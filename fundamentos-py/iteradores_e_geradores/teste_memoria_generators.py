"""
Teste de memoria com Generators
*********
# Funcao usando listar 465 mb
def fib_lista(maximo):
    nums = []
    a, b = 0, 1
    while len(nums) < maximo:
        nums.append(b)
        a, b = b, a + b
    return nums


for n in fib_lista(100000):
    print(n)
***********
# Teste com generator - 2,6 MB
def fib_gen(maximo):
    a, b, contador = 0, 1, 0
    while contador < maximo:
        a, b = b, a + b
        yield a
        contador += 1


for n in fib_gen(100000):
    print(n)

"""


# Funcao usando listas 465 mb
def fib_lista(maximo):
    nums = []
    a, b = 0, 1
    while len(nums) < maximo:
        nums.append(b)
        a, b = b, a + b
    return nums


# Teste com generator - 3 MB
def fib_gen(maximo):
    a, b, contador = 0, 1, 0
    while contador < maximo:
        a, b = b, a + b
        yield a
        contador += 1


for n in fib_gen(100000):
    print(n)
