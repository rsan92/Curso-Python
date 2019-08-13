"""
Hooks - são os testes em si. Ou seja, a execução dos testes.
**********
setUp() -> É executado antes de cada método de teste. É util para criarmos instancias de objetos e outros dados

tearDown() -> É executado ao final de cada método de teste. É util para excluir dados ou fechar conexões com
bancos de dados
"""
import unittest


class ModuloTest(unittest.TestCase):
    def setUp(self) -> None:
        # Configurações do setUp
        pass

    def test_primeiro(self):
        # setUp() vai rodar antes do teste
        # tearDown() vai rodar após o teste.
        pass

    def tearDown(self) -> None:
        # Configurações do tearDown()
        pass


