# Operações diversas
num = soma = num_total = 0

print('-' * 24)
print('Calculadora de valores')
print('-' * 24)
print()

while 0 <= num != 999:
    num = int(input('\033[mInsira um valor\033[1;31m(999 para parar)\033[m:\033[33m '))
    if num == 999:
        continue
    num_total += 1
    soma += num

if num_total > 0:
    print('\033[m\nO total de números inteiros adicionados foi {} e a soma deles resulta em {}.'.format(num_total, soma))
else:
    print('\033[33m\nNenhum número foi adicionado.\033[m')
