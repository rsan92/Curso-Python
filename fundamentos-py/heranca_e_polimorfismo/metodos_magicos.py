"""
POO - Métodos Mágicos

São todos os métodos que utilizam dunder (Double Underscore).
Ex: dunder init -> __init__

"""


class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):  # Retorna a representação do objeto - O padrão é retornar o objeto de memória
        return f'{self.titulo} escrito por {self.autor}'

    def __str__(self):  # Retorna a representação do objeto - O padrão é retornar o objeto de memória
        return self.titulo

    def __len__(self):  # Retorna o tamanho do objeto.
        return self.paginas

    def __del__(self):  # Deleta um objeto da memoria
        print('Um objeto do tipo livro foi deletado da memória')

    def __add__(self, outro):  # Concatena 2 elementos
        return f'{self} - {outro}'

    def __mul__(self, outro):  # Multiplica o elemento
        if isinstance(outro, int):
            msg = ''
            for n in range(outro):
                msg += ' ' + str(self)
            return msg
        return 'Não posso multiplicar'


livro1 = Livro('Teste 1', 'Geek University', 400)
livro2 = Livro('Teste 2', 'Geek University', 350)

print(livro1)
print(livro2)

print(len(livro1))
print(len(livro2))

print(livro1 + livro2)
print(livro1 * 5)

del livro1



