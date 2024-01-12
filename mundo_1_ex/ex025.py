# Detecte "SILVA" em um nome
from cores import Cores as cr

nome = input('Digite um nome: ')
nome = nome.title().strip()

if 'Silva' in nome:
    print(f'{cr.negrito}{nome}{cr.fim}, você tem Silva no seu nome.')

elif nome.isnumeric():
     print(f'{cr.vermelho}Erro. Digite um nome válido{cr.fim}')

else:
    print(f'{cr.f_vermelho}O nome digitado não tem Silva.{cr.fim}')