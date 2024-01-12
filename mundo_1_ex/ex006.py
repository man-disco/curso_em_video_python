# Dobro, triplo e raiz quadrada
from cores import Cores as cr
n = int(input('Digite um número: '))

d = n * 2
t = n * 3
r = n ** (1/2)

print(f'O dobro de {cr.roxo + cr.sublinhado}{n}{cr.fim} é {cr.verde + cr.sublinhado}{d}{cr.fim}, o triplo é {cr.vermelho + cr.sublinhado}{t}{cr.fim} e sua raiz quadrada é {cr.sublinhado + cr.cyano}{r:.2f}{cr.fim}.')