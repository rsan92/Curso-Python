"""
Escrevendo em arquivos CSV

writerow() -> Escreve uma linha
from csv import writer

with open('filmes.csv', 'w') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Titulo', 'Genero', 'Duracao'])
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o Gênero: ')
            duracao = input('Infome a duração: ')
            escritor_csv.writerow([filme, genero, duracao])


"""
# DictWriter
from csv import DictWriter

with open('filmes.csv', 'w', newline='') as arquivo:
    cabecalho = ['Titulo', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o Gênero: ')
            duracao = input('Infome a duração: ')
            escritor_csv.writerow({"Titulo": filme, "Gênero": genero, "Duração": duracao})



