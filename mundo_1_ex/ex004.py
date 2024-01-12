# Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
from cores import Cores as cr

v = input('Digite algo: ')

print(f'\n{cr.sublinhado + cr.amarelo}O tipo primito de{cr.fim} "{cr.negrito + cr.cyano}{v}{cr.fim}" é:{cr.fim} {cr.negativo + cr.branco}{type(v)}{cr.fim}\n')


g = cr.verde + cr.negrito
r = cr.vermelho + cr.negrito

c1 = ''
c2 = ''
c3 = ''
c4 = ''
c5 = ''
c6 = ''
c7 = ''

if v.isnumeric():
    c1 = g
else:
    c1 = r

if v.isspace():
    c2 = g
else:
    c2 = r

if v.isalpha():
    c3 = g
else:
    c3 = r

if v.isdecimal():
    c4 = g
else:
    c4 = r

if v.isupper():
    c5 = g
else:
    c5 = r

if v.islower():
    c6 = g
else:
    c6 = r
    
if v.istitle():
    c7 = g
else:
    c7 = r

print('É um valor numérico? => {}{}{}'.format(c1, v.isnumeric(), cr.fim))
print('É um espaço vazio? => {}{}{}'.format(c2, v.isspace(), cr.fim))
print('É um valor alfabético? => {}{}{}'.format(c3, v.isalpha(), cr.fim))
print('É um valor decímal? => {}{}{}'.format(c4, v.isdecimal(), cr.fim))
print('É um valor em letras maiúsculas? => {}{}{}'.format(c5, v.isupper(), cr.fim))
print('É um valor em letras minúsculas? => {}{}{}'.format(c6, v.islower(), cr.fim))
print('Começa com letra maiúscula? => {}{}{}'.format(c7, v.istitle(), cr.fim))


