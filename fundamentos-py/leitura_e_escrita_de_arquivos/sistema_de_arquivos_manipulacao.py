"""
Sistema de arquivos - Manipulação
**********
# Verifica se um arquivo existe no caminho onde o programa é executado
print(os.path.exists('arquivo.txt'))
print(os.path.exists('texto.txt'))

# Verifica diretório
print(os.path.exists('arquivos_txt'))
print(os.path.exists('arquivos_txt\\geek.txt'))
print(os.path.exists('arquivos_txt\\geek2.txt'))

# Path Relativo
print(os.path.exists('arquivos_txt'))

# Path Absoluto
print(os.path.exists('F:\\0- Programação\\Curso-Python\\fundamentos-py\\leitura_e_escrita_de_arquivos\\arquivos_txt'))

# Criando arquivos
# forma 1
open('arquivo-teste.txt', 'w').close()
# forma 2
open('arquivo-teste2.txt', 'a').close()
# forma 3
with open('arquivo-teste3.txt', 'w') as arquivo:
    pass
# forma 4
os.mknod('arquivo.teste4.txt') # Não funciona em ambiente Win

# Criar diretorio
os.mkdir('templates')  # Caso o nome já exista, teremos um FileExistsError
os.mkdir('templates\\temp2')  # Caso o nome já exista, teremos um FileExistsError

# Criar uma arvore de diretorios
# 'exist_ok=True' faz com que não seja retornado um erro caso a arvore já exista
os.makedirs('templates\\temp\\tempo2', exist_ok=True)

# Renomear diretorio
# Se o diretorio não estiver vazio, teremos um OSError
os.rename('templates\\temp\\tempo2', 'templates\\temp\\geek2')
# Renomear arquivo
os.rename('templates\\temporario\\a.txt', 'templates\\temporario\\b.txt')

# Deletar arquivos
# Ao deletar um arquivo ou diretorio, eles não vão para a lixeira.
# No Win, caso o arquivo esteja em uso, não será possível deletar.
# Caso o arquivo não exista, teremos o FileNotFoundError
# Caso seja informado um diretorio e não um arquivo, teremos um IsADirectoryError
os.remove("templates\\temporario\\b.txt")

# Caso o diretorio não esteja vazio, teremos um OSError
# Caso o diretorio não exista, teremos um FileNotFoundError
os.rmdir('templates\\temporario\\geek2')

# Deletando todos os arquivos de uma pasta
for arquivo in os.scandir('templates'):
    if arquivo.is_file():
        os.remove(arquivo.path)

# Removendo toda a arvore de pastas
os.removedirs('templates\\temporario\\tempo2\\aa')


# Remover arquivo enviandco para a lixeira
os.remove('arquivo-teste.txt')  # Não vai para a lixeira

from send2trash import send2trash
send2trash('arquivo-teste2.txt') # Enviado para a lixeira

# Trabalhando com arquivos e diretorios temporarios
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek University')
    input()

# Em arquivos temporarios só conseguimos escrever bits. por isso é necessario utilizar o b antes da string
import tempfile

with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek University')
    tmp.seek(0)
    print(tmp.read())

# Trabalhando com arquivos e diretorios temporarios

import tempfile

arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'Geek University')

print(arquivo.name)
print(arquivo.read())
input()
arquivo.close()
************
"""
import os, platform





