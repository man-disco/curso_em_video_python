# Comparar valores
from cores import Cores as cr

n1 = float(input(f'{cr.amarelo}Digite um número:{cr.fim} '))
n2 = float(input(f'{cr.verde}Digite outro número:{cr.fim} '))
n3 = float(input(f'{cr.roxo}Digite mais um número:{cr.fim} '))

if n1 > n2 > n3:
    print(f'\nO maior número é o {cr.amarelo}{n1:.0f}{cr.fim}.\nO menor número é o {cr.roxo}{n3:.0f}{cr.fim}.')
elif n1 < n2 > n3:
    print(f'\nO maior número é o {cr.verde}{n2:.0f}{cr.fim}.\nO menor número é o {cr.roxo}{n3:.0f}{cr.fim}.')
elif n1 > n2 < n3:
    print(f'\nO maior número é o {cr.roxo}{n3:.0f}{cr.fim}.\nO menor número é o {cr.verde}{n2:.0f}{cr.fim}.')
elif n3 > n2 > n1:
    print(f'\nO maior número é o {cr.roxo}{n3:.0f}{cr.fim}.\nO menor número é o {cr.amarelo}{n1:.0f}{cr.fim}.')
   
