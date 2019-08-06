"""
POO - Objetos

Objetos-> São instancias da classe.
lamp = Lampada(cor='Branca', voltagem=110, luminosidade=60)
print(f'A lampada está ligada? {lamp.check_lampada()}')
lamp.liga_desliga()
print(f'A lampada está ligada? {lamp.check_lampada()}')

nome = 'usuario 1'
sobrenome = 'us1'
email = 'user1@gmail.com'
senha = '123'

user = Usuario(nome, sobrenome, email, senha)


"""


class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def check_lampada(self):
        if self.__ligada:
            return True
        return False

    def liga_desliga(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz(self):
        print(f'O Cliente {self.__nome} diz: "Olá" ')


class ContaCorrente:
    contador = 499

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'O cliente é {self.__cliente._Cliente__nome}')


class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


cliente = Cliente('Rafael Alves', '123.456.789-10')
cc = ContaCorrente(5000, 10000, cliente)

print(dir(cc))
cc.mostra_cliente()
