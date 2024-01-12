# Radar
from cores import Cores as cr

vel = float(input('Qual a velocidade em que o veículo estava?: '))

limite = 80
ex = vel - limite
multa_km = 7.00 * ex

if vel > limite:
    print(f'{cr.vermelho}O carro x ultrapassou o limite de velocidade de 80 km/h a {cr.fim + cr.negrito}{vel:.0f}km/h.{cr.fim}\nA multa cobrada será no valor de {cr.verde + cr.negrito + cr.sublinhado}R$ {multa_km:.2f}{cr.fim}.')

else:
    print(f'{cr.verde}O carro x permaneceu abaixo do limite de velocidade a {cr.fim + cr.negrito}{vel:.0f} km/h.{cr.fim}')