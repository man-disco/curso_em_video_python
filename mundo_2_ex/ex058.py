# Jogo de adivinhação 2.0
from random import randint

# Número de tentativas
palpites = 0
pnum = 0
num = randint(0, 10) # Número aleatório de 1 a 10 que o computador gera toda vez
print('-' * 40)
print('Estou pensando em um número de 1 a 10')
print('-' * 40)
while num != pnum:
    pnum = int(input('\nDigite o seu palpite> '))
    palpites += 1
    # Verifica se o jogador está perto ou longe do número pensando
    if pnum < num:
        print('Estou pensando em um número maior...')
    elif pnum > num:
        print('Estou pensando em um número menor...')
    else:
        print('\n\033[1;32mVocê acertou!\033[m\n')
print('Você adivinhou o número \033[01;32m{}\033[m com \033[01;34m{}\033[m tentativa{}!\n'.format(num, palpites, "s" if palpites > 1 else "" ))
