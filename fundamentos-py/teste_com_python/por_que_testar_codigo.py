"""
Por que testar o nosso codigo?
Testes Automatizados!
         Aplicacao WEB
-------------------------------
/                             /
/      frontend e backend     /
-------------------------------
/     testes automatizados    /
-------------------------------

Por que testar o nosso codigo?
    - Reduzir bugs no codigo existente
    - Testes garantem que novos recursos não quebrem recursos antigos
    - Testes garantem que bugs que foram corrigidos anteriormente continuem corrigidos
    - Testes garantem que a refatoração não tragam novos bugs

TDD - Test Driven Development
Com o TDD é utilizado estagios de desenvolvimento:
    - Você escreve seu teste primeiro;
    - Então vc escreve o código minimo suficiente para fazer o teste passar;
    - Então refatora o código para realizar a funcionalidade e testa novamente;
    - Uma vez que o teste passe, o recurso é considerado completo
Estagios do TDD:
    - Red; (Test FAIL)
    - Green; (Test OK)
    - Refactory; (Complete code)
"""


class Gato:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f'{self.__nome} está miando')


felix = Gato('felix')
felix.miar()
print(felix.nome)




