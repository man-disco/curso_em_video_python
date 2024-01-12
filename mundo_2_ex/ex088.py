from random import randint
from time import sleep

print('''
  __  __                   ____
 |  \/  | ___  __ _  __ _ / ___| ___ _ __  1.0
 | |\/| |/ _ \/ _` |/ _` | |  _ / _ \ '_ \ ---
 | |  | |  __/ (_| | (_| | |_| |  __/ | | |
 |_|  |_|\___|\__, |\__,_|\____|\___|_| |_|
              |___/
_____________________________________________♥
|Gerador de números aleatórios para a Megasena|
'——-------—–----------------------------------•
''')
palpites = int(input('Quantos jogos pretende fazer?> '))


def rand_game_num(palpites):
    """Gera os 6 números para cada palpite e retorna os valores"""
    try:
        global jogos
        jogos = 0
        for p in range(palpites):
            game = []
            while len(game) < 6:
                num = randint(1, 60)
                if num not in game:
                    game.append(num)
            print(f'\nJogo {jogos+1}º: ', game, end='\n ', flush=True)
            print('\rCtrl + C para fechar\n', flush=True)
            jogos += 1
            sleep(0.4)
            game.clear()
        return jogos

    except KeyboardInterrupt:
        if jogos <= 1:
            print('\n\nFoi gerado apenas um jogo.')
            exit()
        else:
            print(f'\n\nForam gerados {jogos} jogos.')
            exit()


rand_game_num(palpites)

if jogos == 1:
    print('\nFoi gerado apenas um jogo.')
else:
    print(f'\nForam gerados {jogos} jogos.')
