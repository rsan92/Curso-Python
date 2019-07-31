"""
O bloco try/except
Utilizamos para tratar erros que podem ocorrer na execução do código e evita que o sistema pare de funcionar

OBS: Tratar erro generico não é a melhor forma. O ideal é tratar de forma especifica
----
-> Tratamento generico
try:
    //Execucao
except:
    //O que deve ser feito em caso de problema
-
#  Tente executar no try, se der erro, execute o except
try:
    func()
except:
    print("Deu erro")
-
try:
    len(5)
except:
    print("Deu algum problema")
--------
-> Tratamento Especifico
-
a)
try:
    geek()
except NameError:
    print('Você está utilizando uma função inexistente')
-
b)
try:
    len(5)
except TypeError as err:
    print(f'Você está chamando a função de forma errada... {err}')
-
c)
try:
    len(5)
except TypeError as erra:
    print(f'Deu TypeError-> {erra}')
except NameError as errb:
    print(f'Deu NameError-> {errb}')
except:
    print(f'Deu um erro não previsto')

"""


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None


dic = {"nome": "Geek"}
print(pega_valor(dic, "nome"))
print(pega_valor(dic, "game"))  # -> KeyError

