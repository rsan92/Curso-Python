"""
Pacote é um diretório contendo uma coleção de modulos
"""
import sys
sys.path.append("..")
from geek import geek1, geek2
from geek.university import geek3, geek4
print('Teste')

print(geek1.pi)
print(geek1.funcao1(4, 6))

print(geek2.funcao2())
print(geek2.curso)

print(geek3.funcao3())

print(geek4.funcao4())
