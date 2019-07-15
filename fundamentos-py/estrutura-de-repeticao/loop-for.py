"""
for indice, valor in enumerate(nome):
    print(nome[indice], "- ID -", indice)

for _, letra in enumerate(nome):
    print(letra)

for valor in enumerate(nome):
    print(valor)
    print(valor[0])
    print(valor[1])

nome = 'Testes Testando'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

qtd = int(input("Quantos loops?"))
soma = 0
for n in range(1, qtd+1):
    num = int(input(f'Informe o valor {n}/{qtd} valor: '))
    soma = soma + num
print(f'Total: {soma}')
"""
code = "U0001F60D"
emoji = "\U0001F60D"

for n in range(1, 11):
    print(f'{emoji * n}')


