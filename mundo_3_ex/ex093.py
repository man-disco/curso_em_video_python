# Gerenciadomento de jogador de futebol
gols = 0
l = "-"*75
jogador = {}
jogador['nome'] = str(input('Nome: ').strip().capitalize())
jogador['partidas'] = int(input(f'Partidas jogadas por {jogador["nome"]}: '))
jogador['gols'] = list()
for x in range(jogador['partidas']):
    g = int(input(f'0{x+1}ª Partida → Nº de gols: ' if x < 9
                  else f'{x+1}ª Partida → Nº de gols: '))
    jogador['gols'].append(g)
    gols += g
jogador['gols_total'] = gols
print(f'\n{l}\n   {jogador}\n{l}')
for k, v in jogador.items():
    print(f'{k + " tem o valor " + str(v):>50}')
print(f'{l}')
for y, p in enumerate(jogador['gols']):
    print(f'{"Partida":>35} {y+1} •→ {p} gols')
print(f'{l}\n{"Ele fez um total de":>43} {gols} gols.\n{l}\n'
      if gols > 1 else f'{l}\n{"Ele fez apenas um gol :(":^55}\n{l}\n')
