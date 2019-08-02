"""
Leitura de Arquivos
*********************
a)Para ler um arquivo em Python, é necessário abrir ele primeiro.
    - open()-> informamos o nome do arquivo a ser lido. a função retorna um TextIOWrapper
    - Por padrão, a função open() abre o arquivo para a leitura. Se ele não existir, teremos um FileNotFoundError
    - <_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>
    - <class '_io.TextIOWrapper'>
    - A leitura é realizada através de cursor
    - A função read() lê to-do o conteudo do arquivo
-------------------

"""

arquivo = open('texto.txt')
# print(arquivo)
# print(type(arquivo))
print(arquivo.read())
print(arquivo.read())

