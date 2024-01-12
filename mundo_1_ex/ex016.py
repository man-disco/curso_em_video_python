# Porção inteira de um número
from math import floor, trunc
from cores import Cores as cr

num = float(input('Digite um número: '))
print(f'A porção inteira de {cr.negativo}{num}{cr.fim} é {cr.cyano}{floor(num)}{cr.fim}.\n')
# print(f'A porção inteira de {num} é {trunc(num)}.'

