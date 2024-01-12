# Caixa eletrônico
# Notas disponíveis no caixa são: R$ 50, 20, 10 e 1
cedulas = [50, 20, 10, 1]
print('=' * 30)
print(f'\033[6;27m{"Banco EXEMPLO":^30}\033[m')
print('=' * 30)
valor = int(input('Valor do saque> R$ '))

print('=' * 30)

for ced in cedulas:
    if valor // ced > 0:
        print(f'Total de cédulas {valor // ced} de R$ {ced}')
        valor %= ced

print('=' * 30)
print('\nObrigado por usar o nosso caixa! Volte sempre!\n')
