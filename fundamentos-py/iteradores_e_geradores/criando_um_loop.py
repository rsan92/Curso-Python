"""
Criando loop customizado
***********
# Loop padrão
for num in [1, 2, 3, 4, 5]:
    print(num)

for letra in 'Geek University':
    print(letra)
"""
def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


nome = 'Geek University'
meu_for(nome)

numeros = [1, 2, 3, 4, 5]
meu_for(numeros)


