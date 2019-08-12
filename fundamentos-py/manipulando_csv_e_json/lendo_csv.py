"""
Lendo arquivos CSV
CSV - Comma Separeted Values - Valores Separados por Virugla

www.dados.gov.br/dataset
************
# Possivel de se trabalhar, mas não é o ideal.
with open('lutadores.csv', encoding='utf8') as arquivo:
    dados = arquivo.read()
    # print(type(dados)) <class 'str'>
    dados = dados.split(',')[2:]
    print(dados)
***********
A linguagem Python tem 2 formas de trabalhar com arquivos CSV.
1- reader: Permite que iteremos sobre as linhas do arquivo CSV como listas;
2- DictReader: Permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts
***********
# Reader
from csv import reader

with open('lutadores.csv', encoding='utf8') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)  # pular o cabeçalho
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f'{linha[0]}, nasceu no {linha[1]}, e mede {linha[2]} centimetros')
************
# DictReader
from csv import DictReader
with open('lutadores.csv', encoding='utf8') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f"{linha['Nome']}, nasceu no {linha['País']}, e mede {linha['Altura (em cm)']} centimetros")
"""
# DictReader
from csv import DictReader
with open('lutadores.csv', encoding='utf8') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')  # Define o delimitador da lista
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f"{linha['Nome']}, nasceu no {linha['País']}, e mede {linha['Altura (em cm)']} centimetros")




