# Jogo de adivinhação
from random import randint
from time import sleep
from cores import Cores as cr

num = randint(1, 5) # Número aleatório de 1 a 5 que o computador gera toda vez

print('-=-' * 14)
print(f'{cr.azul}Eu estou pensando em um número de 1 até 5{cr.fim}.')
print('-=-' * 14)

cho = int(input('Em qual número eu pensei?> ')) # Número que o jogador chuta
print('Processando...')
sleep(2)

if cho == num: # Se o palpite for igual ao nímero gerado, o jogador ganha
    print(f'{cr.verde}\nParabéns, você acertou!\nO número que eu pensei é o {num}{cr.fim}.')
else:
    print(f'{cr.vermelho}\nVocê errou.\nO numero que eu pensei é o {num}{cr.fim}.')