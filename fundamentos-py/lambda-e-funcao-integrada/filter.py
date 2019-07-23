"""
Filter

Filtrar dados de uma determinada coleção
----
# Exemplo de como tirar média
valores = 1, 2, 3, 4, 5, 6

media = (sum(valores) / len(valores))
print(media)
----
import statistics
valores = 1, 2, 3, 4, 5, 6
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
#media com a função mean()
media = statistics.mean(valores)
print(media)

media = statistics.mean(dados)
print(media)

res = filter(lambda valor: valor > media, dados)  # Retorna os valores acima da media na tupla "dados"; media = 2.18
print(list(res))
"""
# Forma 1 (melhor forma)
paises = ['', 'argentina', '', 'chile', '', 'colombia', '', '','', 'equador']
print(paises)

print("-----Forma1---------(melhor)")
res = filter(None, paises)
print(list(res))

# Forma 2
print("-----Forma2---------")
paises = ['', 'argentina', '', 'chile', '', 'colombia', '', '','', 'equador']
res = filter(lambda pais: len(pais) > 0, paises)
print(list(res))

# Forma 3
print("-----Forma3---------")
paises = ['', 'argentina', '', 'chile', '', 'colombia', '', '','', 'equador']
res = filter(lambda pais: pais != '', paises)
print(list(res))


