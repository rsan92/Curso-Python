"""
POO - Heranca (Inheritance)

A ideia de Herança é de reaproveitar código e também extender nossas classes.

Com a Herança, a partir de uma classe existente, nos extendemos outra classe que passa a herdar atributos
e metodos da classe herdade

Cliente
    - nome;
    - sobrenome;
    - cpf;
    - renda;
Funcionario:
    - nome;
    - sobrenome;
    - cpf;
    - matricula
*************
class Cliente:
    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Funcionario:
    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


cliente1 = Cliente('Rafael', 'Alves', '111.111.111.11', 5000)
funcionario1 = Funcionario('Ian', 'Brito', '222.222.222.22', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())
************
Existe alguma entidade generica o suficiente para encapsular os atributos e metodos comuns a outras entendidades??

"""


class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    """Cliente herda Pessoa"""
    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):
    """Funcionario herda Cliente"""
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    # Sobrescrita
    def nome_completo(self):
        print(super().nome_completo())
        print(self._Pessoa__cpf)
        return f'Funcionario: {self.__matricula} Nome: {self._Pessoa__nome}'


# Sobrescrita de Métodos (Overriding)
# Ocorre quando reescrevemos um metodo presente na super classe ou em classes filhas

cliente1 = Cliente('Rafael', 'Alves', '111.111.111-11', 5000)
funcion1 = Funcionario('Teste', 'T1', '222.222.222-22', 3400)

print(cliente1.nome_completo())
print(funcion1.nome_completo())
