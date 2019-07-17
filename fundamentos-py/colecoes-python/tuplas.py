"""
lista1 = [1, 2, 3, 4, 5, 6]
tupla1 = (1, 2, 3, 4, 5, 6)
tupla2 = 1, 2, 3, 4, 5, 6

print(type(lista1))
print(type(tupla1))
print(type(tupla2))

tupla3 = (4)
tupla4 = 4,
print(type(tupla3))
print(type(tupla4))

tupla5 = tuple(range(11))
print(tupla5)

tupla6 = tuple(range(11, 100,))
print(tupla6)

tupla7 = tuple(range(100, 10, -1))
print(tupla7)

tupla8 = tupla1+tupla2
print(tupla8)
print(tupla1)
print(tupla2)
-------------------
tupla = (1, 2, 3)
print(3 in tupla)
------------------
tupla = (range(15))
for n in (range(50)):
    if n in tupla:
        print(n)

print("--")

for indice, valor in enumerate(tupla):
    print(indice, valor)
-------
aluno = tuple("Rafael Sousa Alves Nobre")
i = 0
while i < len(aluno):
    print(aluno[i])
    i += 1

print(aluno[::-1])

print((aluno.index("R")))

"""

tupla = (1, 2, 3)
nova = tupla
print(nova)
print(tupla)

outra = tupla + nova
print(outra)
