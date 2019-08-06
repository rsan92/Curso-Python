"""
POO - Abstração e Encapsulamento

Objetivo de encapsular nosso codigo dentro de um grupo lógico e hierarquico utilizando classes.
"""


class Conta:
    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador = self.__numero

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisa ser positivo')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente')
        else:
            print('O valor deve ser positivo')

    def transferir(self, valor, conta_destino):
        # 1- Remover da conta origem
        self.__saldo -= valor
        # 2- Adicionar na conta destino
        conta_destino.__saldo += valor


conta1 = Conta('Geek', 150.00, 1500)
conta1.extrato()

conta2 = Conta('University', 300, 2000)
conta2.extrato()

valor = 100
# Forma incorreta
# conta2.sacar(valor)
# conta1.depositar(valor)
# conta1.extrato()
# conta2.extrato()
conta1.transferir(valor, conta2)
conta1.extrato()
conta2.extrato()




