# Conversor de Celsius para Fahrenheit
from cores import Cores as cr
c = float(input('Digite a temperatura desejada em Celsius: '))
f = c * 1.8 + 32
print(f'A temperatura de {cr.verde}{c:.2f}{cr.fim} °C medirá {cr.roxo}{f:.2f}{cr.fim} °F.')