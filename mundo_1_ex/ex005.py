# Sucessor e antecessor
from cores import Cores as cr

n = int(input('Digite um número: '))
a = n - 1
s = n + 1 

print(f'O antecessor de {cr.cyano + cr.negrito}{n}{cr.fim} é {cr.vermelho + cr.negrito}{a}{cr.fim} e o seu sucessor é {cr.negrito + cr.verde}{s}{cr.fim}')