"""
Teste de velocidade com expressoes geradoras
*******
# Generators
def nums():
    for num in range(1, 10):
        yield num


ge1 = nums()
print(ge1)
print(next(ge1))
print(next(ge1))

# Generator Expression
ge2 = (num for num in range(1, 10))

print(ge2)
print(next(ge2))
print(next(ge2))

"""
# Realizando teste de velocidade

import time

# Generator Expression
gen_inicio = time.time()
print(sum(num for num in range(1, 10000000)))
gen_tempo = time.time() - gen_inicio
print(f'Tempo de Expresion:  {gen_tempo}')

# List Comprehension
list_inicio = time.time()
print(sum([num for num in range(10000000)]))
list_tempo = time.time() - list_inicio
print(f'Tempo de Comprehension:  {list_tempo}')

