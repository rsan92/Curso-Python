"""
Conjuntos
---------
Diferença entre Conjuntos(Set) e Mapas(Dicionários:
    . Dicionário tem chave e valor
    . Conjunto tem apenas chave
--------
s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3}) # Não adiciona repetidos
print(s)
print(type(s))

s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

s = set('Rafael')
print(s)
-------
dados = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]

lista = list(dados)
print(f'Lista: {lista}, len: {len(lista)}')

tupla = tuple(dados)
print(f'Tupla: {tupla}, len: {len(tupla)}')

dicionario = {}.fromkeys(lista, 'dict')
print(f'Dicionario: {dicionario}, len:{len(dicionario)}')

conjunto = set(dados)
print(f'Conjunto: {conjunto}, len:{len(conjunto)}')
---------
s = {1, 'b', True, None, 33, 2.95}
print(s)

for valor in s:
    print(valor)
--------
cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']
print(cidades)
print(len(cidades))
print(len(set(cidades)))
-------
s = {1, 2, 3}
s.add(4)
s.add(4)
s.add(4)
s.add(4)
print(s)
------
s = {1, 2, 3, 4}
print(s)
s.remove(2)
s.remove(3)
# s.remove(2) -> KeyError por valor inexistente
print(s)

print('---')

s = {1, 2, 3, 4}
print(s)
s.discard(2)
s.discard(3)
s.discard(3)
print(s)
----
s = {1, 2, 3}
print(s)

novo = s.copy()
novo.add(4)
print(s)
print(novo)

print('--')

s = {1, 2, 3}
print(s)
novo = s
novo.add(4)
print(s)
print(novo)

novo.clear()
print(s)
print(novo)
----
estudantes_py = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_jv = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# nomes unicos em cada curso
unicos = estudantes_jv.union(estudantes_py)
# {'Fernando', 'Patricia', 'Ana', 'Gustado', 'Guilherme', 'Pedro', 'Julia', 'Marcos', 'Ellen'}
# {'Ana', 'Guilherme', 'Julia', 'Ellen', 'Gustado', 'Pedro', 'Marcos', 'Patricia', 'Fernando'}
print(unicos)

unicos2 = estudantes_py | estudantes_jv
print(unicos2)

# nomes duplicados em ambos os cursos
print('----')
ambos = estudantes_jv.intersection(estudantes_py)
print(ambos)

ambos2 = estudantes_py & estudantes_jv
print(ambos2)
# estudantes em apenas um curso
so_py = estudantes_py.difference(estudantes_jv)
so_jv = estudantes_jv.difference(estudantes_py)
print(f'Só jv: {so_jv}')
print(f'Só py: {so_py}')
"""



