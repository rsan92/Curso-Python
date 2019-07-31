"""
PDB - Python Debugger
----
a) "Debugar" com print é uma prática ruim, pois deixa o código sujo e com informações importantes
def dividir(a, b):
    print(f'a={a}, b={b}')
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


print(dividir(4, 7))
print(dividir(2, 0))
print(dividir('4', 'a'))
-
b) Debugando com o PyCharm
def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


print(dividir(4, 7))
print(dividir(2, 0))
print(dividir('4', 'a'))
----
c) Debugando com o PDB em versões abaixo da 3.7
import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Python'
final = nome_completo + ' faz o curso: ' + curso
print(final)
- OU -
nome = 'Angelina'
sobrenome = 'Jolie'
import pdb; pdb.set_trace()  # Importa e executa a função de trace no meio do código
nome_completo = nome + ' ' + sobrenome
curso = 'Python'
final = nome_completo + ' faz o curso: ' + curso
print(final)
----
d) Debugando com breakpoint()
nome = 'Angelina'
sobrenome = 'Jolie'
breakpoint()  # Comando no Python 3.7
nome_completo = nome + ' ' + sobrenome
curso = 'Python'
final = nome_completo + ' faz o curso: ' + curso
print(final)
"""
#  Comandos basicos do PDB
#  l = listar onde estamos no codigo
#  n = proxima linha
#  p <variavel>= imprime variavel
#  c = continua a execucao e finaliza o debug


def soma(l, n, p, c):
    breakpoint()
    return l+n+p+c


print(soma(1, 2, 3, 4))