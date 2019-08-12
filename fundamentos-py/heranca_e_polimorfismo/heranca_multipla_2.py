"""
POO - Heranca Multipla
***********
Pode ser direta ou indireta
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
class Pinguim(Aquatico, Terrestre):  # Herda diretamente de Terrestre e Aquatico, e indiretamente de Animal
    def __init__(self, nome):
        super().__init__(nome)


baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre('Xim')
print(tatu.andar())
print(tatu.cumprimentar())

tux = Pinguim('Tux')
print(tux.andar())
print(tux.nadar())
print(tux.cumprimentar())  # Method Resolution Order - MRO. Eu sou o Tux da terra

print(f'Tux é instancia de Pinguim? {isinstance(tux, Pinguim)}')
print(f'Tux é instancia de Aquatico? {isinstance(tux, Aquatico)}')
print(f'Tux é instancia de Terrestre? {isinstance(tux, Terrestre)}')
print(f'Tux é instancia de Animal? {isinstance(tux, Animal)}')
print(f'Tux é instancia de object? {isinstance(tux, object)}')



