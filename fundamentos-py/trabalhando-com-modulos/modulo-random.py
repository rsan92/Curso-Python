"""
Modulo random
- São outros arquivos Python que podem ser incorporados
- Possui várias funções para geração de números pseudo-aleatórios
-----------
# Forma 1 - Importando por completo (não recomendado)
# Ao realizar o import do modulo por completo, todas as funções ficarão disponiveis(em memoria)
# import random
# print(random.random())

-
# Forma 2 - Importando uma função especifica
from random import random
# random() - Retorna um numero random entre 0 e 1
for i in range(10):
    print(random())
-
# uniform() -> Gerar um numero real aleatorio entre os valores estabelecidos
from random import uniform
for i in range(10):
    print(uniform(5, 10))  # O 7 não é incluido
-
from random import randint
# randint() - Gera valores pseudo-aleatórios entre os valores estabelecidos
from random import randint
for i in range(6):
    print(randint(1, 61), end=', ')
-
# choice() -> Mostra um valor aleatório entre um iterável.
from random import choice
jogadas = ['Pedra', 'Papel', 'Tesousa']
print(choice(jogadas))
-

"""
# shuffle()-> Tem a função de embaralhar dados
from random import shuffle
cartas = ['A', 'B', 'C', 'D', 'E']
print(cartas)
shuffle(cartas)
print(cartas)







