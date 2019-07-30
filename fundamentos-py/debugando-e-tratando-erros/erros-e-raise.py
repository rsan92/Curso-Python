"""
Levantando os própios erros com raise]
raise -> Lança exceções
----
raise TipoDoErro('Mensagem de erro')
    ex: raise ValueError('Valor incorreto')

OBS: Raise finaliza a função
"""
def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('[texto] precisa ser uma String')
    if type(cor) is not str:
        raise TypeError('[cor] precisa ser uma String')
    if cor not in cores:
        raise ValueError(f'[cor] não esperada. tente {cores}')
    print(f'O texto "{texto}" será escrito na cor "{cor}"')


# colore(1, 2)
# colore('Oi', 2)
# colore('Oi', 'preto')
colore('Oi', 'verde')
