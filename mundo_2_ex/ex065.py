# Média
total = soma = media = menor = maior = 0
continuar = 'S'

while continuar in 'Ss':
    num = int(input('Digite um valor: '))
    continuar = str(input('Deseja continuar? [S/N] '))

    soma += num
    total += 1

    if total == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < maior:
            menor = num

media = soma / total

print('\nA soma dos {} valores resulta em {}.'.format(total, soma))
print('O maior valor é o {}.\nO menor valor é o {}.'.format(maior, menor))
print('A média dos valores resulta em {:.2f}.'.format(media))
