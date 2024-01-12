# Cálculo de seno e cosseno de um ângulo
from math import sin, cos, tan, radians
from cores import Cores as cr

ang = float(input(f'{cr.sublinhado}Digite o ângulo que você deseja calcular:{cr.fim} '))

sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))

print(f'\nO seno de {cr.amarelo}{ang}{cr.fim} é {cr.negrito + cr.vermelho}{sen:.2f}{cr.fim}.')
print(f'O cosseno de {cr.verde}{ang}{cr.fim} é {cr.negrito + cr.azul}{cos:.2f}{cr.fim}.')
print(f'A tangente de {cr.roxo}{ang}{cr.fim} é {cr.negrito + cr.cyano}{tan:.2f}{cr.fim}.')