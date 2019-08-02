"""
StringIO
********
- Para poder ler ou escrever dados, o sofware e o SO precisam ter permissão para isso.
"""
from io import StringIO
mensagem = 'Este é apenas uma string normal\n'

# Podemos criar um arquivo em memória já com uma String inserida

arquivo = StringIO()
# Mesma coisa de open('arquivo.txt, 'w')
arquivo.write(mensagem)
arquivo.write('Outro texto')
arquivo.seek(0)
print(arquivo.read())







