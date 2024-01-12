# Dissecando um número
from cores import Cores as cr


try:
    num = int(input('Digite um numero entre 1 a 9999: '))
    
    if num <= 9999 and num % 10 != 0:

        u = num // 1 % 10
        d = num // 10 % 10
        c = num // 100 % 10
        m = num // 1000 % 10

        print(f'{cr.azul}A unidade de {num} é {cr.fim + cr.sublinhado}{u}{cr.fim}.')
        print(f'{cr.cyano}A dezena de {num} é {cr.fim + cr.sublinhado}{d}{cr.fim}.')
        print(f'{cr.roxo}A centena de {num} é {cr.fim + cr.sublinhado}{c}{cr.fim}.')
        print(f'{cr.verde}O milhar de {num} é {cr.fim + cr.sublinhado}{m}{cr.fim}.')

    else:
        print(f'{cr.vermelho + cr.negrito}[Erro!] Tente novamente números válidos.{cr.fim}')

except ValueError:
    print(f'{cr.vermelho + cr.negrito}[Erro!] Tente novamente somente com números.{cr.fim}')