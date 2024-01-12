# Sorteio de alunos
from random import choice
from cores import Cores as cr

a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')

lista = [a1, a2, a3, a4]
escolhido = choice(lista)


print(f'{cr.branco}O aluno sorteado para apagar o quadro é{cr.fim} {cr.verde + cr.sublinhado}{escolhido}{cr.fim}.')
