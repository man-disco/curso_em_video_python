# Gerenciadomento de jogador de futebol (com vários jogadores :-D)
gols = 0
esc_jog = None
l = "-"*75
jogador = {}
jogadores = []
print('\033[1;7mRelação de jogadores\033[m')
while True:
    jogador['nome'] = str(input('\nNome: ').strip().capitalize())
    jogador['partidas'] = int(input(f'Partidas jogadas por {jogador["nome"]}: '))
    jogador['gols'] = list()
    for x in range(jogador['partidas']):
        g = int(input(f'0{x+1}ª Partida → Nº de gols: ' if x < 9
                      else f'{x+1}ª Partida → Nº de gols: '))
        jogador['gols'].append(g)
        gols += g
    jogador['total'] = gols
    gols = 0
    jogadores.append(jogador.copy())
    cont = str(input('\nContinuar? [S/n]: ').lower())
    if cont == 's' or cont == '':
        continue
    else:
        break
print('-'*40)
print('id ', end='')
for k in jogador.keys():
    if k != 'partidas':
        print(f'{k:<15}', end='')
print('\n' + '-'*40)
for p, j in enumerate(jogadores):
    del j['partidas']
    print(f'{p+1:<2} ', end='')
    for v in j.values():
        print(f'{str(v):<15}', end='')
    print()
print('-'*40)
while True:
    esc_jog = int(input('\nQual jogador deseja consultar? (0 para fechar): '))
    if esc_jog == 0:
        break
    if esc_jog > len(jogadores) or esc_jog < 0:
        print('\033[31mErro! Escolha um id de jogador válido!\033[m')
        continue
    jogador = jogadores[esc_jog-1]
    print(f'\n{l}\n {" Levantamento do/a Jogador/a " + jogador["nome"]:^70}\n{l}')
    for y, p in enumerate(jogador['gols']):
        print(f'{"Partida":>35} {y+1} •→ {p} gols')
    print(f'{l}\n{"Ele/a fez um total de":>43} {jogador["total"]} gols.\n{l}\n'
    if jogador['total'] > 1 else f'{l}\n{"Ele fez apenas um gol :(":^50}\n{l}\n')

