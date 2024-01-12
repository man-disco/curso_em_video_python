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
gen = 0
game = []
games = []

try:
    guesses = int(input('Quantos jogos pretende fazer?> '))
    for g in range(guesses):
        while len(game) < 6:
           num = randint(1, 60)
           if num not in game:
               game.append(num)
        games.append(game[:])
        game.clear()

    for generated in games:
        print(f'\nJogo {gen+1}º:', generated, end='\n ', flush=True)
        print('\rCtrl + C para fechar\n', flush=True)
        sleep(0.4)
        gen += 1
except ValueError:
    print('lmao')

if gen == 1:
    print('\nFoi gerado apenas um jogo.')
else:
    print(f'\nForam gerados {gen} jogos.')

