"""
PEP8 - Python Enhancement Proposal

Propostas de melhorias para a linguagem Python

The Zen of Python

>> import this

Pontos de atenção:
1- CamelCase para nome de classes;
2- Utilizar nomes em minisculo para funcoes ou variaveis
3- Utilizar 4 espaços para identar o codigo (CUIDADO COM O "TAB"!!!)
4- Se atentar as linhas em branco no codigo
    . Separar funcoes e definicoes de classe com duas linhas em branco
    . Metodos dentro de uma classe devem ser separados por apenas uma linha em branco
5- Imports devem ser sempre feitos em linhas separadas e sempre devem vir no topo do codigo
6- Nao deixar espaços em instrucoes e expressoes
"""
import sys
import os
import funcoes.teste

from types import GeneratorType, BuiltinFunctionType

from types import(
    GetSetDescriptorType,
    SimpleNamespace,
    AsyncGeneratorType
)

class Teste:
    print("Teste")
    pass


class TesteETestando:
    print("Teste e Testando")
    pass


def soma(a):
    print(a+1)
    pass


def soma_dois(a, b):
    print(a+b)
    pass


def verifica_string(texto):
    if 'a' in texto:
        print('Tem "A" na palavra: ', texto)

    else:
        print('Não tem "A" na palavra: ', texto)
    pass


Teste()
TesteETestando()

c = 3
d = 4

soma(c)
soma_dois(c, d)

verifica_string('Teste')
verifica_string('Banana')

funcoes.teste.validarcpf('123456')
