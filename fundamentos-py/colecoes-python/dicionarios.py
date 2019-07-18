"""
Mapas - Coleções do tipo chave x valor
----
print(type({}))
----
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
paises2 = dict(br='Brasil', eua='Estados Unidos', py="Paraguai")


localidades = {
    (35.6895, 39.6917): 'Escritorio em Tokio',
    (40.7128, 74.0060): 'Escritorio em Nova York',
    (37.7749, 122.4194): 'Escritorio em São Paulo'
}
buscar = (35.6895, 39.6917)
print(localidades.get(buscar))
---------
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)

receita['abr'] = 350
print(receita)

novo_dado = {'mai': 500}
receita.update(novo_dado)
print(receita)

receita.update({'jun': 150})
receita.update({'mai': 100})
print(receita)
receita.update({'mai': 550})
print(receita)
--------------
receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
ret = receita.pop('jan')
print(ret)
print(receita)

del receita['fev']
print(receita)
-------------------
carrinho = []
produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['God of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

produto1 = ('PlayStation 4', 1, 2300.00)
produto1 = ('God of War 4', 1, 150.00)

carrinho = (produto1, produto2)
print(carrinho)

carrinho = []
produto1 = {'nome': 'PlayStation 4', 'quantidade': 1, 'preco': 2300.00}
produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'preco': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)
"""
d = dict(a=1, b=2, c=3)
novo = d.copy()
novo['d'] = 4
# print(d)
# print(novo)

outro = {}.fromkeys(['nome', 'idade', 'sexo'], None)
print(outro)

veja = {}.fromkeys('teste', 'valor')
print(veja)
