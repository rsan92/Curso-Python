"""
import math

def area(r):
    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]
ares = []
for r in raios:
    ares.append(area(r))

print(ares)

# Forma MAP
areas = map(area, raios)
print(list(areas))

# Forma MAP com Lambda
print(list(map(lambda r: math.pi * (r ** 2), raios)))
----
cidades = [('Berlin', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26)]
print(cidades)

# f = 9/5 * C + 32
c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)
print(list(map(c_para_f, cidades)))
"""
nome_sobrenome = [('Rafael', 'Alves'), ('Gustavo', 'Henrique'), ('Joao','Maria'), ('Teste','Testando')]
print(nome_sobrenome)

nome_completo = lambda nc: (nc[0] + ' ' + nc[1])
nome_invertido = lambda ni: (ni[-1] + ' ' + ni[0])
print(list(map(nome_completo, nome_sobrenome)))
print(list(map(nome_invertido, nome_sobrenome)))

