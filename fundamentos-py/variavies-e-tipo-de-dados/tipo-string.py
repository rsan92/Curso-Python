"""
Tipo String
"""
nome1 = "Teste1"
nome2 = """Teste2"""
nome3 = 'Teste3 Espaço3'
nome4 = '''Teste4'''

print(f'{nome1} , {nome2}, {nome3}, {nome4}')

print(nome1.lower())
print(nome2.upper())
print(nome3.split()[0], nome3.split()[1])
print(nome4[2:])
print(nome1[::-1])
print(nome3.replace('e', '3'))

