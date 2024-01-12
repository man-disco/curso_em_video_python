from time import sleep
from random import randint


# Faça um programa que tenha duas funções, uma sorteia números e
# a outra soma eles
numeros = []


def sorteia(lista):
    print('Números sorteados: ', end='')
    while len(lista) < 5:
        rnum = randint(1, 10)
        lista.append(rnum)
        print(rnum, end=' ', flush=True)
        sleep(0.2)
    print('\033[3m- Fin\033[m')


def somaPar(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
            color = 1
        else:
            color = 2
        print(f'\033[{color}m{num}\033[m', end=' ')
    print(f'- A soma de todos os valores \033[1mpares\033[m é {soma}.')


sorteia(numeros)
somaPar(numeros)
