# Cálculo de cateto e hipotenusa de um triangulo
from math import sqrt, hypot
from cores import Cores as cr

bc = float(input(f'{cr.amarelo}Digite o comprimento do cateto oposto: '))
ac = float(input(f'{cr.fim + cr.roxo}Digite o comprimento do cateto adjacente: '))

hip = pow(bc, 2) + pow(ac, 2)
hip = sqrt(hip)

print(f'{cr.fim}\n\A soma dos quadrados dos catetos {cr.amarelo}{bc:.0f}{cr.fim} e {cr.roxo}{ac:.0f}{cr.fim} resultam na raiz da hiponetusa {cr.verde}√{pow(bc, 2) + pow(ac, 2):.0f}{cr.fim}, que mede {cr.cyano}{hip:.2f}{cr.fim}.')
# print(f'Somando o quadrado dos catetos resulta em {hypot(bc, ac):.2f}.')
