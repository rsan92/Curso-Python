"""
while expressao_boolean
    -execucao do loop
---------
-> Exemplo 1:
num = 1
while num != 0:
    num = int(input("Informe um numero:"))
    print(num)
---------
-> Exemplo 2:
num = 1
while num < 10:
    print(num)
    num += 1

"""
resposta = ''
while resposta != 'sim':
    resposta = input("Acabou?")
    print(resposta)

