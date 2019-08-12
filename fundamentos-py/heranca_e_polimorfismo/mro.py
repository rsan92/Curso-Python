"""
POO - Method Resolution Order - MRO
É a ordem de execução dos métodos (quem será executado primeiro)

Podemos conferir a ordem de 3 formas:

* Via propriedade da classe __mro__
* Via método mro()
* Via help
"""


class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Olá, eu sou {self.__nome}'


class Aquatico(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar'


class Terrestre(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando'

    def cumprimentar(self):
        return f'Eu sou o {self._Animal__nome} da terra'


# A ordem da herança altera a MRO da classe Pinguim
class Pinguim(Terrestre, Aquatico):  # Herda diretamente de Terrestre e Aquatico, e indiretamente de Animal
    def __init__(self, nome):
        super().__init__(nome)


tux = Pinguim('Tux')

# Pinguim(Aquatico, Terrestre) = Eu sou Tux do mar
# Pinguim(Terrestre, Aquatico) = Eu sou o Tux da terra
print(tux.cumprimentar())


