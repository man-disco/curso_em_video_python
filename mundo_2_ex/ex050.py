# Soma entre somente os números pares
s = 0

for i in range(1, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n

print('A soma total de todos os números pares é {}'.format(s))