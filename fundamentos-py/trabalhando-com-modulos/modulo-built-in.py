"""
Trabalhando com modulos built-in: Modulos integrados
________________________
|Python|Modulos builtin|
************************
----
import random as rdm  # Alias de importação
print(rdm.random())
----
from random import *
print(random())
----
import random
print(random.random())
----
from random import randint as rdi, random as rdm
print(rdi(5, 89))
print(rdm())
----
from random import (
    random,
    randint,
    shuffle
)
print(random())
print(randint(1, 10))
lista = ['a', 'b', 'c', 'd']
shuffle(lista)
print(lista)
----

----
----
----
----
----
"""


