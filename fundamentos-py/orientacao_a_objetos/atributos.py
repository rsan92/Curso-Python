"""
POO - Atributos
Tipos:
    - Atributos de Instância
    - Atributos de Classe
    - Atributos Dinâmicos

* Em Python, todos os atributos de uma classe sao publicos (podem ser acessados em to-do o projeto.
Caso queira definir um atributo como privado, utiliza-se o "__" no inicio do seu nome. (Name Mangling)
**********************************
# Atributos de instancia: São atributos declarados dentro do construtor
user = Acesso('user@gmail.com', '1234')
print(user.email)
print(user.mostra_email())

# print(user.__senha)  # AttributeError
# print(dir(user))
print(user._Acesso__senha)  # Name Mangling - Forma incorreta
print(user.mostra_senha())


# Atributos de Instancia:
# Significa que, ao criarmos instancias/objetos de uma classe, todas as instancias terão estes atributos

user1 = Acesso('user1@gmail.com', '1234')
user2 = Acesso('user2@gmail.com', '5678')

print(user1.mostra_email())
print(user2.mostra_email())
**************************************
# Atributos de Classe:
# São atributos que são declarados diretamente na classe, fora do construtor.
# Geralmente ja inicializamos um valor, que é compartilhado em todas as instancias da classe.
# Todas as instancias terão o mesmo valor para esse atributo
class Produto:
    imposto = 1.05  # 0,05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


p1 = Produto('PlayStation 4', 'Video Game', 2500)
p2 = Produto('Xbox', 'Video Game', 4500)

print(p1.valor)
print(p1.id)
print(p2.valor)
print(p2.id)
# Não precisamos criar uma instancia para fazer acesso a um atributo de classe
print(Produto.imposto)

"""


class Lampada:
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Atributos publicos e privados
class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha  # atributo privado

    def mostra_senha(self):
        return self.__senha

    def mostra_email(self):
        return self.email


class Produto:
    imposto = 1.05  # 0,05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


# Atributos Dinamicos




