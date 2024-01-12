# Aumento de salário
from cores import Cores as cr

sal = float(input(f'Digite o salário do funcionário: {cr.verde}R$ '))

if sal > 1250:
    print(f'{cr.fim}\nCom o aumento de {cr.negrito}10%{cr.fim} o salário do funcionário fica {cr.negrito + cr.verde}R$ {sal * 0.10 + sal:.2f}{cr.fim}.')
else:
    print(f'{cr.fim}\nCom o aumento de {cr.negrito}15%{cr.fim} o salário do funcionário fica {cr.negrito + cr.verde}R$ {sal * 0.15 + sal:.2f}{cr.fim}.')