# Sorteio de apresentação de alunos
from random import shuffle, sample
from cores import Cores as cr

a1 = input(f'{cr.cyano}Primeiro aluno: {cr.fim}')
a2 = input(f'{cr.roxo}Segundo aluno: {cr.fim}')
a3 = input(f'{cr.vermelho}Terceiro aluno: {cr.fim}')
a4 = input(f'{cr.verde}Quarto aluno: {cr.fim}')

lista = [a1, a2, a3, a4]
lista = sample(lista, len(lista))

print(f'\n{cr.f_azul}A ordem da apresentação dos trabalhos será:{cr.fim}\n{cr.sublinhado}{lista}{cr.fim}')
