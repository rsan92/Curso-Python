"""
Try / Except / Else / Finally
----
TODA ENTRADA DE DADOS DEVE SER TRATADA
----
try:
    num = int(input("informe um numero: "))
except ValueError:
    print('Valor incorreto.')
else:
    print(f'você digitou: {num}')
Só entra no ELSE se não entrar no EXCEPT
----
try:
    num = int(input("informe um numero: "))
except ValueError:
    print('Valor incorreto.')
else:
    print(f'você digitou: {num}')
finally:  # ->Sempre é executado após o except ou else. Geralmente utilizado para fechar ou desalocar recursor do pgm
    print("Finaly!")

print("Depois do try/except")
----
Exemplo tratando execpts:
def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possivel realizar uma divisão por zero'


num1 = input("Informe o primeiro numero: ")
num2 = input("Informe o segundo numero: ")

print(dividir(num1, num2))
-
Exemplo tratando except de forma generica
def dividir(a, b):
    try:
        return int(a) / int(b)
    except:
        return 'Ocorreu um erro'


num1 = input("Informe o primeiro numero: ")
num2 = input("Informe o segundo numero: ")

print(dividir(num1, num2))

"""

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema {err}'


num1 = input("Informe o primeiro numero: ")
num2 = input("Informe o segundo numero: ")
print(dividir(num1, num2))
