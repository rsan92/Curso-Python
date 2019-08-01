"""
Modulos Customizados: Modulos Python são arquivos .py
----
#funcao especifica
from funcoes_parametro import soma_impares

print(soma_impares([1, 2, 3, 4, 5, 6, 7, 8, 9]))
"""
import funcoes_parametro as fp  # Importando to do o modulo e dando um alias

print(fp.lista)  # acessando uma variavel de dentro de funcoes_parametro
print(fp.soma_impares(fp.lista))

