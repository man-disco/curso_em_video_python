# Tupla de números - De novo!
numeros = ()
numeros_pares = ()
for i in range(1, 6):
    numero = int(input('Digite um valor=> '))
    numeros += numero,
    if numero % 2 == 0:
        numeros_pares += numero,
    print(numeros)

if numeros.count(9) > 0:
    print(f'O número 9 apareceu {numeros.count(9)} ', end='vezes.\n' if numeros.count(9) > 1 else 'vez.\n')
else:
    print('O número 9 não está na tupla.')
if 3 in numeros:
    print(f'O número 3 está na posição {numeros.index(3) + 1}.')
else:
    print('O número 3 não consta na tupla.')
if len(numeros_pares) > 1:
    print(f'Os números pares foram: {numeros_pares}')
else:
    print('Não existem números pares na tupla.')