# Números primos

# número de divisíveis
m = 0

num = int(input('Digite um número inteiro: '))

for i in range(1, num+1):
    if num % i == 0:
        print('\033[1;33m', end='')
        m += 1     
    else:
        print('\033[0;31m', end='')
    print(f'{i}', end=' ')
if m == 2: 
    print('\n\033[1;32mO número \033[1;33m{}\033[32m é primo porque ele foi divisível por \033[1;33m{}\033[32m números.\033[m'.format(num, m))
else:
    print('\n\033[31mO número \033[1;33m{}\033[31m não é primo porque ele foi divisível por \033[1;33m{}\033[31m números.\033[m'.format(num, m))