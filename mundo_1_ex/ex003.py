# Exercício Python 003: Crie um programa que leia dois números e mostre a soma entre eles
from cores import Cores as cr
num1 = int(input(cr.azul + "Digite um valor: \033[m"))
num2 = int(input(cr.cyano + "Digite outro valor: \033[m"))

soma = num1 + num2

print("A soma de {}{}{} com {}{}{} é igual a {}{}{}.".format(cr.negrito + cr.azul, num1, '\033[m',cr.negrito + cr.vermelho, num2, '\033[m', cr.negrito + cr.amarelo, soma, cr.fim))