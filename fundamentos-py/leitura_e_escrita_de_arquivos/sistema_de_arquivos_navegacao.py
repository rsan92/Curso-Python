"""
Sistema de Arquivos e Navegação
**********
Para fazer uso da manipulação de arquivos no sistema operacional, precisamos importar e fazer uso do modulo OS.
----
OS -> Operating System
----
# getcwd() -> pega o current work directory
print(os.getcwd())

# isabs -> verificar se o diretorio é absoluto
print(os.path.isabs('C:\\Projetos-Pessoais\\Curso-Python\\fundamentos-py'))

# chdir() -> mudar o diretorio
os.chdir('..')
print(os.getcwd())
-------
import os, platform

print(platform.uname()) # Informações da máquina
print(os.name)  # posix(Linux e Mac) / nt (Win)
-----------
print(os.getcwd())
res = os.path.join(os.getcwd(), '..\\', 'geek', 'university')
os.chdir(res)
print(os.getcwd())
---------
print(os.listdir())
print(len(os.listdir()))
print(list(os.scandir('arquivos_txt')))
----------

"""
import os

scanner = os.scandir()

arquivo = list(scanner)
# print(arquivo)
# print(dir(arquivo[0]))

print(arquivo[0].inode())  # Identificação do objeto na arvore de objetos
print(arquivo[0].is_dir())  # É um diretório?
print(arquivo[0].is_file())  # É um arquivo?
print(arquivo[0].is_symlink())  # É um link simbolico?
print(arquivo[0].name)  # Nome do arquivo
print(arquivo[0].path)  # Caminho até o arquivo
print(arquivo[0].stat())  # Estatísticas sobre o arquivo

scanner.close()  # É necessário fechar a var com o scandir()
