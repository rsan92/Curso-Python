"""
POO - Propriedades - Properties
"""

class Conta:
    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite


conta1 = Conta('Rafael', 3000, 5000)
conta2 = Conta('Rafa', 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())

# soma = conta1._Conta__saldo + conta2._Conta__saldo  ERRADO!
soma = conta1.get_saldo() + conta2.get_saldo()
print(f'Soma das contas {soma}')

