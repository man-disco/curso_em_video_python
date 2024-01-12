from cores import Cores as cr
# Aumento de salário
sal = float(input('Qual o salário atual do funcionário? R$ '))
aum = 15
cont = sal + (sal * 15 / 100)

print(f'\nPara o funcionário que atualmente ganha R$ {cr.sublinhado + cr.verde}{sal:.2f}{cr.fim} com o aumento de {cr.amarelo}{aum}%{cr.fim} ficará R$ {cr.sublinhado + cr.azul}{cont:.2f}{cr.fim}.')