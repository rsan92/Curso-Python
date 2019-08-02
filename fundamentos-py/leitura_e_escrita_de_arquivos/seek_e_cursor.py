"""
Seek e Cursor
***************
seek()-> Utilizado para movimentar o cursor pelo arquivo
----
arquivo = open('texto2.txt', encoding='utf8')
print(arquivo.read())
print(arquivo.read())
********
#  seek (): indica em qual caracter queremos colocar o cursor
arquivo.seek(22)
print(arquivo.read())
********
# readline(): lê o arquivo linha por linha.
print(arquivo.readline())

ret = arquivo.readline()
print(ret)
print(type(ret))
**********
# readlines():
ret = arquivo.readlines()
print(f'Linhas do arquivo: {len(ret)}')
print(ret)
**********
# Passos para se trabalhar com arquivo
# 1- Abrir o arquivo
arquivo = open('texto2.txt', encoding='utf8')

# 2- Processar o arquivo
print(arquivo.read())

print(arquivo.closed)  # Verifica se o arquivo está fechado; True = fechado, False = aberto

# 3- Fechar o arquivo
arquivo.close()
print(arquivo.closed)
"""
arquivo = open('texto2.txt', encoding='utf8')
print(arquivo.read(50))  # Leitura dos 50 primeiros chars





