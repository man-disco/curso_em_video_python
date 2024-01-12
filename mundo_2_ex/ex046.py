# Contagem regressiva de fogos de artifício
from emoji import emojize, emoji_list
from time import sleep

try:
    s = int(input('Quantos segundos para a contagem dos fogos?: '))
    for c in range(s, 0, -1):
        print('{} segundos para o ano novo...'.format(c), emojize(':party_popper:'))
        sleep(1)
    print(emojize(':collision:'))
    sleep(0.5)
    print(emojize('\n:fireworks: :collision: :fireworks: {}Feliz Ano Novo!!{} :fireworks: :collision: :fireworks:\n'.format('\033[1;35m', '\033[m')))
    sleep(0.5)
    print(emojize(':collision:'))

except KeyboardInterrupt:
    print('\n\033[1;31mNum esperou :(\033[m')