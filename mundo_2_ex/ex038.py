# Comparando números (denovo)

num1 = float(input('Digite um número: ')) 
num2 = float(input('Digite outro número: '))

if num1 > num2:
    print(f'\nO primeiro número é maior.')
elif num2 > num1:
    print(f'\nO segundo número é maior.')
else:
    print('\nOs dois números são iguais.')