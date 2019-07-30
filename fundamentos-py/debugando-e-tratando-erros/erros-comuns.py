"""
Erros mais comuns em Python
-----------
SyntaxError: Algo que o python não reconhece como parte da linguagem
-
a) Sem () na definição da função
def funcao:
    print('Olá mundo')
-
b) None é uma palavra reservada do Python
None = 1
----------
NameError: Ocorre quando uma variavel ou função não foi definida
-
a) "variavel" é uma var não declarada anteriormente
print(variavel)
-
b) Função não definida anteriormente
func()
-
c) Nunca vai entrar no loop pois "msg" só é definido se a < 10
a = 18
if a < 10:
    msg = "É maior que 10"
print(msg)
---------
TypeError: Ocorre quando uma função/operação é aplicada a um tipo errado
-
a) len() não aceite um tipo "int"
print(len(5))
-
b) Não é possivel iterar String e uma lista vazia
print('geek' + []
----------
IndexError: Ocorre quando tentamos acessar um elemento em um dado indexado e informamos um indice inválido
-
a) Indice 10 não existe na lista; Out of range
lista = [0,1,2]
print(lista[10])
---------
ValueError Ocorre quando uma função built-in recebe argumentos com o tipo correto e o valor inapropiado
-
a) int() Espera um número na função
print(int("Geek"))
----------
KeyError: Ocorre quando tentamos acessar um dicionario com uma chave inexistente
-
a) o dicionario "dic" está vazio, e a chave "a" não existe no momento do print.
dic = {}
print(dic['a'])
----------
AttributeError: Ocorre quando uma variavel não tem um atributo/função
-
a) Tuple não tem a função .sort()
tupla = (11, 2, 31, 4)
print(tuple.sort)
----------
IdentationError: Ocorre quando não respeitamos a indentação do Python (4 espaços)
-
a) Após definir a func, o print deveria estar 4 espaços indentado
def func():
print('olá mundo')
"""




