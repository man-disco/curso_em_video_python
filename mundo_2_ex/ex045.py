# Pedra, papel, tesoura
from random import sample
from time import sleep

jogadas = ['pedra', 'papel', 'tesoura']

cpu = sample(jogadas, 1)
cpu = str(cpu)[2:-2]

print('\n\033[21mPedra Papel ou Tesoura\n\033[m')

p1 = input('Digite sua jogada (\033[1;34mpedra\033[m, \033[1;35mpapel\033[m, \033[1;37mtesoura\033[m): ').lower()

if p1 != 'pedra' and p1 != 'papel' and p1 != 'tesoura':
    print('\n\033[31mEscolha uma das alterativas acima.\033[m')

else:
    print(f'\nO computador está pensando\n')

    # Cria os três pontos sinalizando que o computador está computando uma resposta
    for i in range(3):
        print('.', end='', flush=True)
        sleep(0.8)

    # Cor da escolha do jogador
    col1 = ''
    # Cor da escolha do computador
    col2 = ''

    # Iguala as cores iniciais das opções com as escolhas dos jogadores
    if p1 == 'pedra' and cpu == 'papel':
        col1 = '\033[1;34m'
        col2 = '\033[1;35m'

    elif p1 == 'papel' and cpu == 'pedra':
        col1 = '\033[1;35m'
        col2 = '\033[1;34m'
    
    elif p1 == 'pedra' and cpu == 'tesoura':
        col1 = '\033[1;34m'
        col2 = '\033[1;37m'

    elif p1 == 'tesoura' and cpu == 'pedra':
        col1 = '\033[1;37m'
        col2 = '\033[1;34m'
    
    elif p1 == 'tesoura' and cpu == 'papel':
        col1 = '\033[1;35m'
        col2 = '\033[1;37m'
    
    else:
        col1 = '\033[1;34m'
        col2 = '\033[1;37m'

    print(f'\n\nVocê escolheu {col1}{p1}\033[m')
    print(f'O computador escolheu \033[1m{col2}{cpu}\033[m')

    # Pedra > Tesoura < Pedra
    if p1 == "pedra" and cpu == "tesoura":
        print(f'\n{col1}Pedra\033[m ganha de {col2}tesoura\033[m, \033[1;32mvocê venceu!\033[m\n')
    elif p1 == "tesoura" and cpu == "pedra":
        print(f'\n{col1}\033[mTesoura perde pra {col2}pedra\033[m, \033[1;31mvocê perdeu!\033[m\n')

    # Papel > Pedra < Papel
    elif p1 == "papel" and cpu == "pedra":
        print(f'\n{col1}Papel\033[m ganha de {col2}pedra\033[m, \033[1;32mvocê venceu!\033[m\n')
    elif p1 == "pedra" and cpu == "papel":
        print(f'\n{col1}Pedra\033[m perde pro {col2}papel\033[m, \033[1;31mvocê perdeu!\033[m\n')

    # Tesoura > Papel < Tesoura
    elif p1 == "tesoura" and cpu == "papel":
        print(f'\n{col1}Tesoura\033[m ganha do {col2}papel\033[m, \033[1;32mvocê venceu!\033[m\n')    
    elif p1 == "papel" and cpu == "tesoura":
        print(f'\n{col1}Papel\033[m perde pra {col2}tesoura\033[m, \033[1;31mvocê perdeu!\033[m\n')

    # Empate 
    else:
        print(f'\n\033[1;37mOs dois jogadores escolheram {col2}{cpu}\033[m\n\n\033[1;33mOs dois empataram, ninguém venceu!\033[m\n')