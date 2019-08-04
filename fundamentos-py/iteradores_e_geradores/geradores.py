"""
Geradores
*************
- Geradores (generators) são Iterators (iteradores);
- Generators podem ser criados com funcoes geradoras;
- Funcoes geradores utilizam a palavra reservada yeild;
- Generators podem ser criados por Expressões Geradoras;

Diferenças entre Funcções e Generator Functions
---------------------------------------------------------------------------------
- Funcoes                               / Generator Function                    -
---------------------------------------------------------------------------------
- Utilizam Return                       / utilizam yield                        -
- Retornam uma vez                      / podem utilizar yield multiplas vezes  -
- Quando executada, retorna um valor    / Quando executada, retorna um generator-
---------------------------------------------------------------------------------
*****
def conta_ate(valor_maximo):  # Funcao Geradora
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1


gen = conta_ate(5)
print(type(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

gen = conta_ate(10)
print(next(gen))

print('Geek')

for num in gen:
    print(num)
"""
def conta_ate(valor_maximo):  # Funcao Geradora
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1


gen = list(conta_ate(10))
print(gen)



