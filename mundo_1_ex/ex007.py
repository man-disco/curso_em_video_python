# Media de aluno
from cores import Cores as cr
s_01 = float(input('Primeira nota do aluno: '))
s_02 = float(input('Segunda nota do aluno: '))
s_03 = float(input('Terceira nota do aluno: '))
s_04 = float(input('Quarta nota do aluno: '))

media = (s_01 + s_02 + s_03 + s_04) / 4

print(f'A média das notas {cr.amarelo}{s_01}{cr.fim}, {cr.vermelho}{s_02}{cr.fim}, {cr.cinza}{s_03}{cr.fim} e {cr.azul}{s_04}{cr.fim} resultam em {cr.verde}{media}{cr.fim}.')
