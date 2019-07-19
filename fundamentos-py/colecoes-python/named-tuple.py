"""

"""
from collections import namedtuple

# Formas de declamar nomedtuple
cachorro1 = namedtuple('cachorro1', 'idade raca nome')
cachorro2 = namedtuple('cachorro2', 'idade, raca, nome')
cachorro3 = namedtuple('cachorro3', ['idade', 'raca', 'nome'])

var1 = cachorro1(idade=2, raca='Chow-chow', nome='Ray')
print(var1)
print(var1[0])
print(var1[1])
print(var1[2])

print('---')
var2 = cachorro2(idade=3, raca='Poodle', nome='Pudim')
print(var2)
print(var2.idade)
print(var2.raca)
print(var2.nome)

print('---')
var3 = cachorro3(idade=7, raca='Pitbull', nome='Pit')
print(var3)
print(var3.index('Pit'))
print(var3.index('Pit'))
