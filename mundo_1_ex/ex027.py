# Partição de nome
from cores import Cores as cr

nome = input('Digite seu nome: ').title()
nome = nome.split()
print(f'''\nSeu primeiro nome é {cr.negrito + cr.azul}{nome[0]}.
{cr.fim}Seu último nome é {cr.fim + cr.negrito + cr.verde}{nome[-1]}.''')