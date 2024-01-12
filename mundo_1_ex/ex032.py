# Ano bissexto
ano = int(input('Digite o ano desejado: '))
from cores import Cores as cr

if (ano % 4 == 0) and (ano % 100 != 0):
    print(f'O ano {cr.sublinhado}{ano}{cr.fim} {cr.verde + cr.negrito}é bissexto{cr.fim}.')
else:
    print(f'O ano {cr.sublinhado}{ano}{cr.fim} {cr.vermelho + cr.negrito}não é bissexto{cr.fim}.') 