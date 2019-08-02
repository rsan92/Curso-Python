"""
With
    - É utilizado para criar um contexto de trabalho, onde os recursos utilizados são fechados após o bloco with
**********
"""

with open('texto2.txt', encoding='utf8') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)

print(arquivo.closed)  # O arquivo é fechado após a saída do bloco with
