# Tuplas de números e index
num_ext = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 
           'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

index = int(input(f'Digite um número de 0 até {len(num_ext) - 1}> '))
while index < 0 or index > len(num_ext) - 1: 
    print('\033[mEscolha um número válido!\033[m')
    index = int(input(f'Digite um número de 0 até {len(num_ext) - 1}> '))
    continue

print(f'Você escolheu o número {(num_ext[index])}.')
