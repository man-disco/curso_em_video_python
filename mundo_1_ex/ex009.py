# Tabuada python
from cores import Cores as cr
from math import log10, floor

print(cr.sublinhado + 'Tabuada Python' + cr.fim + '\n')
num = int(input('Digite o número a ser calculado: '))

# Calcula o número vezes 10 + o tamanho do número em caractéres para que a tabela acompanhe o tamanho das multiplicações
print(f'{cr.tachado} {cr.fim}' * (floor(log10(num)+1 * 10) + floor(log10(num)+1)))
for i in range(1, 11):
    print(f'{cr.verde}{num}{cr.fim} x {cr.amarelo}{i}{cr.fim} = {cr.vermelho}{num*i}{cr.fim}')
print(f'{cr.tachado} {cr.fim}' * (floor(log10(num)+1 * 10) + floor(log10(num)+1)))
