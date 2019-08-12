"""
POO - Polimorfismo

Poli -> Muitas
Morfis -> Formas

Objetos que podem possuir muitas formas / Se comportar de formas diferentes
"""

class Animal(object):

    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A Classe filha precisa implementar esse método')

    def comer(self):
        return f'{self.__nome} está comendo'


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        return f'{self._Animal__nome} fala au au'


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        return f'{self._Animal__nome} fala miau'


class Rato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        return f'{self._Animal__nome} está falando...'


felix = Gato('Felix')
print(felix.comer())
print(felix.falar())

pluto = Cachorro('Pluto')
print(pluto.comer())
print(pluto.falar())

mickey = Rato('Mickey')
print(mickey.comer())
print(mickey.falar())



