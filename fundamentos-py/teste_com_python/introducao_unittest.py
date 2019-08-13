"""
Introducao ao modulo Unittest -> Testes unitários

O que são testes unitários? É a forma de se testar unidades individuais de código fonte. Podendo ser:
Funções, metodos, classes, modulos, etc

Para criar nossos testes, criamos classes que herdam de unittest.TestCase, e a partir de então ganhamos todos os
'assertions' presentes no modulo.

Para rodar os testes, utilizamos unittest.main()
*************************
# Conhecendo as assertions
-----------------------------------------------------
Metodo                          Verifica se
assertEqual(a,b)                a == b
assertNotEqual(a,b)             a != b
assertTrue(x)                   x é True
assertFalse(x)                  x é False
assertIs(a,b)                   a é b
assertIsNot(a,b)                a não é b
assertIsNone(x)                 x é None
assertIsNotNone(x)              x não é None
assertIn(a,b)                   a está em b
assertNotIn(a,b)                a não está em b
assertIsInstance(a,b)           a é instancia de b
assertIsNotInstance(a,b)        a não é instancia de b
-------------------------------------------------------
***************
Por convenção, todos os testes devem começar com test_

# Para executar os testes com unittest no modo verbose
python nome_do_modulo -v

# Podemos acrescentar docstrings nos testes
"""






