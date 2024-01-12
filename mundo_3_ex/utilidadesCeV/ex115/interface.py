from . import utilidades as ut
from . import sistema as st
from os import system, name


def linha(tamanho):
    """
    Mostra uma linha na tela com o tamanho desejado.

    :param tamanho: Inteiro que define o tamanho da linha
    """
    print('-'*tamanho)


def titulo(texto='Menu'):

    sz = len(texto) * 10
    linha(sz)
    print(f'{ut.cores["negrito"]}{texto:^{sz}}{ut.cores["fim"]}')
    linha(sz)


def mensagem(texto, espaço=0, erro=True):
    """
    Printa uma mensagem com cores definidas.

    :param texto: Texto que será mostrado
    :param espaço: Valor inteiro que define o espaçamento da mensagem (centralizado)
    :param erro: Booleano que irá definir a cor, erro por padrão
    """
    if erro:
        cor = ut.cores['vermelho'] + ut.cores['negrito']
        print(f'{cor:^{espaço}}{texto}{ut.cores["fim"]}')
    else:
        cor = ut.cores['verde'] + ut.cores['negrito']
        print(f'{cor:^{espaço}}{texto}{ut.cores["fim"]}')
    

def menu(opts=ut.opts):
    """
    teste
    """
    while True:
        titulo()
        for pos, opt in enumerate(opts):
            print(f'{ut.cores["negrito"]}{ut.cores["azul"]}'
                    f'{pos+1:>10}{ut.cores["fim"]} - {opt}')
        linha(40)
        try:
            esc = int(input('\nComando> '))
            if esc == 1:
                st.cadastrar()
            elif esc == 2:
                st.visualizar()
            elif esc == 3:
                system(st.limpa(name))     
                pass
            elif esc == 4:
                print('Saindo...\n')
                break
            else:
                system(st.limpa(name))
                mensagem('Escolha inválida.', 21)
        except ValueError:
            system(st.limpa(name))
            mensagem('Digite um valor inteiro válido!', 14)
        except KeyboardInterrupt:
            esc = input(('\nDeseja sair do programa? [S/N]: '))
            if esc in 'Ss':
                print('Saindo...')
                break
            elif esc in 'Nn':
                system(st.limpa(name))
            else:
                system(st.limpa(name))
                mensagem('Escolha inválida.', 21)

