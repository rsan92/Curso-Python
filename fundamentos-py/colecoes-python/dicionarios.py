"""
Mapas - Coleções do tipo chave x valor
----
print(type({}))
----

"""
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
paises2 = dict(br='Brasil', eua='Estados Unidos', py="Paraguai")

print(paises['br'])

for _, valor in enumerate(paises):
    print(valor)
