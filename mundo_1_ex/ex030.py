# Par ou ímpar
from cores import Cores as cr

print(f'{cr.negrito + cr.amarelo}--= {cr.fim + cr.negativo}Par ou ìmpar{cr.fim + cr.negrito + cr.roxo} =--{cr.fim}\n')
num = int(input('Digite um número: '))

if (num % 2) == 0:
    print(f'{cr.amarelo}Seu número é PAR.{cr.fim}')
else:
    print(f'{cr.roxo}Seu número é ÍMPAR.{cr.fim}')