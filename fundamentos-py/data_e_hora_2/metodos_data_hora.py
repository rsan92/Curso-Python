"""
from textblob import TextBlob


def formata_data(data):
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate('pt-br')} de {data.year}"


hoje = datetime.datetime.today()
print(formata_data(hoje))
***************
nascimento = datetime.datetime.strptime('10/04/1998', '%d/%m/%Y')
print(nascimento)

nascimento2 = input('Qual a sua data de nascimento? ')
nasce = datetime.datetime.strptime(str(nascimento2), '%d/%m/%Y')
print(nasce)
print(type(nasce))
*****
# Exclusivo para trabalhar com horas
almoco = datetime.time(12, 30, 0)
print(almoco)
********

# Marcando o tempo de execucao do código com timeit
# Parametro 1 = String com o comando a ser executado
# Parametro 2 = Number, com o numero de vezes a ser executado o parm 1

# Loop for
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(tempo)

# List Comphension
tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(tempo)

# Map
tempo = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(tempo)



"""
import datetime
import timeit, functools


def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4
    return soma


# print(teste(5))
print(timeit.timeit(functools.partial(teste, 2), number=10000))

