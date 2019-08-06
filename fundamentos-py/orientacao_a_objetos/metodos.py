"""
POO - Metodos: Representam os comportamentos do objeto. Ações que ele pode realizar no sistema
Podem ser "Metodos de instancia" ou "Metodos de classe"
***************
- O metodo "__init__" é um metodo especial usado para construir objetos
- Os metodos dunder(__x__) são chamados metodos magicos
- Não é aconselhavel criar metodos com a nomenclatura dunder, para nao confundir com os ja existentes no PY
***************
Metodo de Instancia:
p1 = Produto('xbox', 'video game', 2300)
print(p1.desconto(50))

print(Produto.desconto(p1, 50))


user1 = Usuario('User1', 'Usuario 1', 'user1@gmail.com', '123')
user2 = Usuario('User2', 'Usuario 2', 'user2@gmail.com', '456')
print(user1.nome_completo())
print(Usuario.nome_completo(user2))

print(f'Senha do usuario 1 {user1._Usuario__senha}')  # Forma errada de acessar um atributo de classe

nome = input("Informe o nome: ")
sobrenome = input("Informe o sobrenome: ")
email = input("Informe o email: ")
senha = input("Informe a senha: ")
senhac = input("Confirme a senha: ")
if senha == senhac:
    user = Usuario(nome, sobrenome, email, senha)
    print('Usuario criado com sucesso')
    senha = input('Informe a senha de acesso: ')
    if user.checa_senha(senha):
        print('Acesso permitido')
else:
    print('Senha não confere')

"""


class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador += self.__numero


class Produto:
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com o desconto"""
        return (self.__valor * (100 - porcentagem)) / 100


from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:
    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f'Temos {cls.contador} usuários no sistema')

    @staticmethod
    def definicao():
        return 'UXR344'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=2000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuario criado: {self.__gera_usuario()}')

    def nome_completo(self):
        return f'{self.__nome}  {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):
        return self.__email.split('@')[0]


# Metodos de Classe
user1 = Usuario('user1', 'usuario 1', 'user1@gmail.com', '123')

Usuario.conta_usuarios()  # Forma correta
user1.conta_usuarios()  # Forma incorreta

print(user1.contador)
print(user1.definicao())



