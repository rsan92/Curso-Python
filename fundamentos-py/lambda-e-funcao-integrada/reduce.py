"""
Não é mais uma função integrada (built-in) e é necessário importar atarvés do modulo 'functools'
Na maioria das vazes, o loop "for" é mais simples de utilizar

Para entender o reduce():
dados = [a1,a2,a3 .... an]
funcao(x , y)
    return x * y
a funcao reduce() deve atuar da seguinte forma:
    passo 1: res1(a1, a2) = aplica a funcao nos dois primeiros elementos e guarda o resultado
    passo 2: res2(res1, a3) - aplica a funcao passando o resultado do passo 1 e o terceiro elemento
    .....
    passo n: resn(resn, an)
"""
from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

multi = lambda x, y: x * y
res = reduce(multi, dados)
print(res)

res = 1
for n in dados:
    res = res * n
print(res)



