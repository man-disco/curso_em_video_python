# Conversor de moeda.
from cores import Cores as cr
print(f'{cr.verde}=$=${cr.fim} {cr.branco + cr.negrito}Conversor de moeda{cr.fim} {cr.verde}$=$={cr.fim}\n')
# Última atualização de válores: 02/03/23 - 19:28

try:
    print(f'1. Converter {cr.verde}real{cr.fim} para {cr.vermelho}dólar{cr.fim}'
    f'\n2. Converter {cr.vermelho}dólar{cr.fim} para {cr.verde}real{cr.fim}'
    f'\n3. Converter {cr.vermelho}dólar{cr.fim} para {cr.azul}euro{cr.fim}'
    f'\n4. Converter {cr.azul}euro{cr.fim} para {cr.verde}real{cr.fim}\n')

    # Valores de conversão de cada moeda
    usd_brl = 5.20
    usd_eur = 0.94
    eur_brl = 5.51

    e = int(input(f'Escolha uma opção: {cr.negrito}'))

    if e == 1:
        val = float(input(f'{cr.fim}\nQuantia de reais para converter para dólar: BRL '))
        print(f'\nCom BRL {val:.2f} você consegue USD {val/usd_brl:.2f}.')

    elif e == 2:
        val = float(input(f'{cr.fim}\nQuantia de dólares para convertem em real: USD '))
        print(f'\nCom USD {val:.2f} você consegue BRL {val*usd_brl:.2f}.')

    elif e == 3:
        val = float(input(f'{cr.fim}\nQuantia de dólares para converter em euro: USD '))
        print(f'\nCom USD {val:.2f} você consegue EUR {usd_eur*val:.2f}.')

    elif e == 4:
        val = float(input(f'{cr.fim}\nQuantia de euros para converter em real: EUR '))
        print(f'\nCom EUR {val:.2f} você consegue BRL {eur_brl*val:.2f}.')

    else:
        print(f'\n{cr.fim + cr.vermelho}Escolha inválida, tente novamente.')
        
except ValueError:
    print(f'\n{cr.fim + cr.vermelho}Escolha inválida, tente novamente.')
    