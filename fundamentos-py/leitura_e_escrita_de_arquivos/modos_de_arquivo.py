"""
Modos de Abertura de arquivo
*************************
r -> Abre para leitura - padrão
**
w -> Abre para escrita e sobrescreve caso o arquivo já exista
**
x -> Abre para escrita somento se o arquivo não existir
# Caso o arquivo exista, gera FileExistsError
try:
    with open('arquivos_txt/university.txt', 'x', encoding='utf8') as arquivo:
        arquivo.write('Teste de conteudo')
except FileExistsError:
    print('Arquivo já existe')
**
a -> Abre para escrita e adiciona no final caso já exista. Se o arquivo não existir, será criado.
    O conteudo será adicionado sempre no final do arquivo, não sendo possível controlar o cursor

with open('arquivos_txt/teste_a', 'a', encoding='utf8') as arquivo:
    while True:
        fruta = input('Digite uma fruta ou sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break
********************
+ -> Abre um arquivo com atualização, leitura e escrita

"""
with open('arquivos_txt/outro.txt', 'r+', encoding='utf8') as arquivo:
    arquivo.write('adicionada\n')
    arquivo.seek(11)
    arquivo.write('2 Nova linha\n')
    arquivo.seek(12)
    arquivo.write('2 Nova linha novamente\n')







