"""
dicionario = {'Curso': 'Programação em Python: Essencial'}
print(dicionario['Curso'])
print(dicionario['Outro']) #keyError
"""
from collections import defaultdict

dicionario = defaultdict(lambda: 'Inexistente')

dicionario['curso'] = 'Programação em Python'

print(dicionario)

print(dicionario['outro'])

