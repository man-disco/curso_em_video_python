# Exercício Python 002: Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas
from cores import Cores as cr
nome = input('Digite seu nome: ')
print('{}É um prazer te conhecer, {}{}!{}'.format(cr.verde, cr.azul, nome, cr.fim))
    