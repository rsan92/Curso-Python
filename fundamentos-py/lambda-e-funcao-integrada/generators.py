"""
Generators
--------
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']


#  List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

#  Generator
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)
-------
from sys import getsizeof

#  Gerando lista de números com list comprehension
lst_comp = getsizeof([x * 10 for x in range(1000)])

#  Gerando lista de números com set comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

#  Gerando lista de números com dict comprehension
dic_comp = getsizeof({x: x * 10 for x in range(1000)})

#  Gerando lista de números com gen comprehension
gen_comp = getsizeof(x * 10 for x in range(1000))

print(f"List: {lst_comp} bytes")  # 4516
print(f"Set: {set_comp} bytes")   # 16500
print(f"Dic: {dic_comp} bytes")   # O mais pesado - 20544
print(f"Gen: {gen_comp} bytes")   # O mais leve - 64

print(getsizeof('Geek'))
print(getsizeof(9))
print(getsizeof(999999886547325))
print(getsizeof(True))
"""
# Iterando com gen
gen = (x * 10 for x in range(1000))
print(gen)

for num in gen:
    print(num)
