# Formatador de nome
from cores import Cores as cr
nome = str(input(f'{cr.negrito}Qual é o seu nome? > {cr.fim}'))

# Nome em letras maíusculas
nome = nome.upper()
print(f'\n{cr.amarelo}Seu nome em letras maíusculas é {nome.strip()}{cr.fim}.')

# Nome em letras minúsculas
nome = nome.lower()
print(f'{cr.azul}Seu nome em letras minúsculas é {nome.strip()}{cr.fim}.')

# Mostre o número de caracteres do nome (sem espaços)
n1 = nome.strip()
n2 = n1.replace(" ", "")
print(f'{cr.verde}{n1.title()} seu nome é formado por {cr.fim}{cr.sublinhado}{len(n2)} letras{cr.fim}.')

# Mostre o número de caracteres do primeiro nome apenas
nome = nome.split()
nome = nome[0].capitalize()
print(f'{cr.vermelho}{nome}{cr.fim} seu primeiro nome é composto por {cr.cyano}{len(nome)}{cr.fim} letras.')
