# Classificação de times
from cores import Cores as cr
times = [
         'botafogo', 'palmeiras', 'grêmio', 'flamengo', 'fluminense',
         'brangantino', 'atletico-pr', 'fortaleza', 'atletico-mg',
         'fortaleza', 'cuiába', 'são paulo', 'cruzeiro', 'corinthians',
         'internacional', 'góias', 'bahia', 'santos', 'vasco da gama',
         'curitiba'
        ]

line = '-'*65
times_org = list(times)
times_org = sorted(times_org)

print(f'{line}' + '\n|' + f'{cr.negrito}'
      f'{"Classificação Brasileirão Série A":^63}'
      f'{cr.fim}' + '|\n|' + f'{line[:-2]}', end='|\n|')

print(f'{cr.negrito + cr.f_verde}{"Os 5 primeiros colocados":^63}'
      f'{cr.fim}' + '|\n|' + f'{line[:-2]}', end='|\n|')

for time in times:
    if times.index(time) < 5:
        print(f'{str(time).capitalize():^12}', end='')
print(f'\t|\n|' + f'{line[:-2]}', end='|\n|')

print(f'{cr.negrito + cr.f_azul}{"Os 4 últimos colocados":^63}'
      f'{cr.fim}' + '|\n|' + f'{line[:-2]}', end='|\n|')

for pos in range(0, len(times)):
    if pos > 15:
        print(f'{str(times[pos]).capitalize():^15}', end='')
print('\t|\n|'+'-'*63, end='|\n|')

print(f'\033[1;7m{"Lista de times":^63}\033[m'
      f'|\n|' + '-'*63, end='|\n')

for time in times_org:
    print(f'|{str(time).capitalize():^63}', end='|\n')
print(f'{line}')


cs = str(input('\nPesquisar posição de time> ')).lower().strip()
while cs not in times:
    print(f'{cr.amarelo}Erro! Esse time não está na lista!{cr.fim}')
    cs = str(input('\nPesquisar posição de time> ')).lower().strip()

print(f'\nO time {cs.capitalize()} está na posição'
      f' {times.index(cs)+1}')
