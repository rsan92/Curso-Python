"""
def cores_favoritas(**kwargs):
    for pessoa,cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')
----
def cumprimento_especial(**kwargs):
    if 'rafael' in kwargs and kwargs['rafael'] == 'Python':
        return 'Bem vindo ao Python'
    elif 'rafael' in kwargs:
        return f'{kwargs["rafael"]} Geek!'
    return 'Não sei quem é você'

print(cumprimento_especial())
print(cumprimento_especial(rafael='Python'))
print(cumprimento_especial(rafael='Oi'))
print(cumprimento_especial(rafael='Teste'))
----
def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome.title()} tem {idade} anos')
    print(args)
    if solteiro:
        print('solteiro')
    else:
        print('casado')
    print(kwargs)


print(minha_funcao(8, 'julia'))

print(minha_funcao(19, 'carla', 8, 4, 3, java=False, python=True))
-------
def mostra_info(a, b, instrutor='Geek', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]


print(mostra_info(1, 2, 3, sobrenome="University", cargo="instrutor"))
----
def mostra_nomes(**kwargs):
    return f'{kwargs["nome"]} {kwargs["sobrenome"]}'


nomes = {'nome': 'Rafael' , 'sobrenome': 'Alves'}

print(mostra_nomes(**nomes))

"""
def soma_multiplos_numeros(a, b, c):
    print(a + b + c)


lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)

dicionario = dict(a=1, b=2, c=3)
soma_multiplos_numeros(*dicionario)
soma_multiplos_numeros(**dicionario)

