"""
--------------------------
Recebendo dados o usuario
--------------------------
input() sempre retorna uma String
- Aspas simples; ('nome')
- Aspas duplas; ("nome")
- Aspas simples triplas ('''nome''')
- Aspas duplas triplas (" ""nome"" ")
"""

# Entrada
# print("Digite o seu nome: ")
# nome: str = input()

nome = input('Qual o seu nome? \n')
# Print no Python 2.x
# print("Seja bem-vindo(a): %s" % nome)

# Print no Python 3.x
# print("Seja bem-vindo(a) {0}".format(nome))

# Print no Python 3.7
print(f'Seja bem-vindo(a) {nome}')


# print("Qual a sua idade?")
idade = input('Qual a sua idade? \n')
# Processamento
# Saida de dados
print(f'{nome} tem {idade} ano(s)')
print(f'{nome} nasceu em {2019 - int(idade)}')


