"""
Escrevendo em arquvos
***********
- Ao abrir um arquivo como leitura, não podemos realizar escrita.
- Assim como, se abrirmos um arquivo como escrita, não podemos realizar leituras
- Ao abrir um arquivo para escrita, o arquivo é criado caso ele não exista
- Abrindo um arquivo com o modo 'w', caso o arquivo já exista, ele será apagado e recriado
*************
# Forma Pythonica
with open('novo.txt', mode='w', encoding='utf8') as arquivo:
    arquivo.write('Novos dados.\n')
    arquivo.write('Outro Podemos colocar quando linhas quisermos.\n')
    arquivo.write('Mais outra Essa é a ultima linha. \n')

arquivo = open('novo.txt', encoding='utf8')
print(arquivo.readlines())
arquivo.close()
****************
# Forma tradicional e não Pythonica
arquivo = open('mais.txt', 'w')

arquivo.write('Um texto qualquer.\n')
arquivo.write('Mais um texto')

arquivo.close()
**********
with open('geek.txt', 'w', encoding='utf8') as arquivo:
    arquivo.write('Geek ' * 1000)

"""
with open('arquivos_txt/frutas.txt', 'w', encoding='utf8') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != "sair":
            arquivo.write(fruta + '\n')
        else:
            break

