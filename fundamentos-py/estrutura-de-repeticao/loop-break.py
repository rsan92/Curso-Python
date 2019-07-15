"""
-Exemplo 1:
for numero in range(1, 11):
    if numero == 9:
        print("vou sair no 9")
        break
    elif numero == 6:
        print("numero 6")
    else:
        print(numero)

"""

while True:
    comando = input("Digite 'sair' para sair: ")
    if comando == "sair":
        break

