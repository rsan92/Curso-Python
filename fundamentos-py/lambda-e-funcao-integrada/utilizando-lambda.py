"""
São funcoes sem nomes / anonimas
----
def funcao(x):
    return 3 * x + 1


print(funcao(4))
print(funcao(7))

calc = lambda x: 3 * x + 1
print(calc(4))
print(calc(7))
----
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

nome = input("Qual o seu nome?")
sobrenome = input("Qual o seu sobrenome?")

print(f'Seu nome completo é: {nome_completo(nome,sobrenome)}')
--------
teste = lambda: 'Python'
uma = lambda x: 3 * x + 1
duas = lambda x, y: (x * y) ** 0.5
tres = lambda x, y, z: 3 / (1 / x+1 / y+1 / z)

print(teste())
# print(uma(6, 5)) -> TypeError por ter mais parametros que o previsto
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))
-------
autores = ['Isaac Asimov', 'Ray Bradbory', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert', 'Orson Scott Card',
           'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']
print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)

"""

# Funcoes quadraticas
# f(x) = a * x ** 2 + b * x + c
def geradora_funcao_quadratica(a, b, c):
    """Retorna a função f(x) = a*x**2+b*x+c"""
    return lambda x: a * x ** 2 + b * x + c


teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))

print(geradora_funcao_quadratica(3, 0, 1)(2))







