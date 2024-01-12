# Progressão Aritmética 3.0
contador = 1
mais = 10
total = 0

numero = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))

while mais != 0:
    total += mais
    while contador <= total:
        print(numero, end=' → ')
        numero += razão
        contador += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar depois do {}? '.format(numero)))
print('\nA progressão aritmética terminou mostrando {} termos.'.format(total))