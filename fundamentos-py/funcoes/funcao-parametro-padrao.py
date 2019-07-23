"""
def exponencial(numero=4, potencia=2):
    return numero ** potencia

print(exponencial(2, 3))
print(exponencial(3))
print(exponencial(3, 5))
print(exponencial())
-------
def soma(num1=5, num2=3):
    return num1 + num2


print(soma(4, 3))
print(soma(4))
print(soma())
----
def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Pensei que voce era o instrutor'
    return f'Olá {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao('Ozzy'))
--------
def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, fun=soma):
    return fun(num1,num2)

def subt(num1, num2):
    return num1 - num2


print(mat(2, 3))
print(mat(2, 3, subt))
----

nome = 'Rafael'

def diz_oi(nome=nome):
    return f'Oi {nome}'


print(diz_oi())
print(diz_oi('Matheus'))
----
total = 0
def incrementa():
    global total
    total = total + 1
    return total


print(incrementa())
"""
contador = 0
def fora():
    contador = 0
    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()

print(fora())
print(fora())
print(fora())

