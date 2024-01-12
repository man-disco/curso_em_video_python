# Cálculo de gasto de viagem
from cores import Cores as cr

dist = float(input('Distância percorrida em km/h na viagem: '))

pas = 0.45 * dist

if dist <= 200:
    pas = 0.50 * dist
    print(f'O custo da passagem ficou em {cr.negrito + cr.verde}R$ {pas:.2f}{cr.fim}.')

else:
    print(f'O custo da passagem ficou em {cr.negrito + cr.verde}R$ {pas:.2f}{cr.fim}.')