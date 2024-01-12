# Par ou ímpar
from random import randint; from time import sleep
jogo = True
jogadas = ['par', 'impar', 'ímpar']
vitorias = 0

while jogo == True:
    # Definições do jogador
    print('-' * 50)
    num_jogador = int(input('Escolha um número de 1 a 9> '))
    # Opções do jogador -> Validações de dados °1
    if num_jogador > 9 or num_jogador <= 0:
        print('-' * 50)
        print('\033[33mEscolha um número até 9!\033[m')
        continue

    jogada_jogador = str(input('Par ou impar?> ')).lower().strip()
    # Opções do jogador -> Validações de dados °2
    while jogada_jogador not in jogadas:
        print('-' * 50)
        print('\033[33mErro, escolha par ou impar!\033[m')
        print('-' * 50)
        jogada_jogador = str(input('Par ou impar?> ')).lower().strip()

        continue

    print('-' * 50)
    print(f'O jogador escolheu \033[1;36m{jogada_jogador}\033[m e jogou o número \033[1;32m{num_jogador}\033[m!')
    print('-' * 50)
    # Definições da máquina
    num_cpu = randint(1, 9)
    if jogada_jogador == 'par':
        jogada_cpu = 'impar'
    else:
        jogada_cpu = 'par'

    print('O computador está pensando...')
    sleep(3)
    print(f'O computador escolheu o \033[1;34m{jogada_cpu}\033[m e jogou o número \033[1;31m{num_cpu}\033[m!')
    print('-' * 50)

    soma = num_jogador + num_cpu

    # Conta a pontuação se o jogador vencer ou para o programa se ele perder uma vez
    if jogada_jogador == 'par' and soma % 2 == 0:
        print('\033[1;32mVocê venceu!\033[m')
        vitorias += 1
    elif jogada_jogador == 'impar' and soma % 2 == 1:
        print(f'\033[1;32m{"Você venceu! :D":^50}\033[m')
        vitorias += 1
    else:
        print(f'\033[1;31m{"Você perdeu! :(":^50}\033[m')
        jogo = False
    
print('-' * 50)
print(f'Você teve {vitorias} vitorias até perder.')
print('-' * 50)

