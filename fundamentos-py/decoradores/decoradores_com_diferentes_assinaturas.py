"""


def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá eu sou o/a {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor.'


print(saudacao('Rafael'))
print(ordenar('Picanha', 'Arroz'))  # TypeError, pois forma enviados 2 parametros para uma funcao que espera 1
********
def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Eu gostaria de {principal} com {acompanhamento}'


print(saudacao('rafael'))
print(ordenar('Picanha', 'Arroz'))


@gritar
def lol():
    return 'lol'


print(lol())

"""


def verifica_primeiro_argumento(valor):
    def internal(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto. Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return internal


@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)


@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2


print(soma_dez(1, 21))
print(soma_dez(10, 12))

print(comida_favorita('pizza', 'churrasco'))
print(comida_favorita('churrasco', 'pizza'))








