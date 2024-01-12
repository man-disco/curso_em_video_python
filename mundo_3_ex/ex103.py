# Ficha de jogador
def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gols.')


n = str(input('Nome: '))
g = str(input('Gols: '))

# Checa se o nome é um número ou está vazio
if n.isnumeric() or n.strip() == '':
    n = '<desconhecido>'
# Checa se o valor de gols é um número
if g.isnumeric():
    g = int(g)
else:
    g = 0
# Checa se a quantia de gols é menor que zero ou se o valor é vazio
if g <= 0:
    g = 0


ficha(n, g)

