# Criando um triângulo
from cores import Cores as cr
print(f'{cr.negrito}-·{cr.fim}' * 12 + '\nAnalisador de triângulos\n' + f'{cr.negrito}-·{cr.fim}' * 12)
a = float(input('\nDigite o valor da primeira reta: '))
b = float(input('Digite o valor da segunda reta: '))
c = float(input('Digite o valor da terceira reta: '))


if a < b + c and b < a + c and c < a + b:
    print(f'\n{cr.verde}As retas acima formam um triângulo{cr.fim}.')
else:
    print(f'\n{cr.vermelho}As retas acima NÃO formam um triângulo{cr.fim}.')