# Metros, centímetros e milímetros
from cores import Cores as cr
from math import floor
v = float(input(f'{cr.negrito + cr.cyano}Digite um valor em metros para ser medido: {cr.fim}'))

s =  cr.negrito + 25 * '-' + cr.fim

mm = v * 1000
cm = v * 100
dm = v / 10
hm = v / 100
km = v / 1000

print(f'\n{s}\n{cr.sublinhado + cr.roxo}{v:.2f}{cr.fim} metros equivalem a:\n{s}\n'
f'{cr.sublinhado}{cr.amarelo}{mm:.0f}{cr.fim} milímetros.\n{s}\n'
f'{cr.sublinhado}{cr.cinza}{cm:.0f}{cr.fim} centímetros.\n{s}\n'
f'{cr.sublinhado + cr.vermelho}{dm:.1f}{cr.fim} decâmetros.\n{s}\n'
f'{cr.sublinhado + cr.branco}{hm:.2f}{cr.fim} hectômetros.\n{s}\n'
f'{cr.sublinhado + cr.cyano}{km}{cr.fim} quilômetros.\n{s}\n')