"""
Decorators / Decoradores
************************
- Decorators sao funcoes
- Envolvem outras funcoes e aprimoram seus comportamentos
- Decorators sao exemplos de Higher Order Functions
- Decorators tem uma sintaxe propria, usando "@" (Syntact Sugar)
************************
def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você')
        funcao()
        print('Tenha um ótimo dia')
    return sendo


def saudacao():
    print('Seja bem vindo(a)')


# Testando 1
teste = seja_educado(saudacao)

# teste()

# Testando 2
def raiva():
    print('EU TE ODEIO')


raiva_educada = seja_educado(raiva)
raiva_educada()
**********
# Syntax Sugar
def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_mesmo

@seja_educado_mesmo
def apresentando():
    print('Meu nome é Pedro')


# Testando
# apresentando()


@seja_educado_mesmo
def dormir():
    print('Quero dormir...')


dormir()

"""




