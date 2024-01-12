# Sistema de pagamentos

print('\nSistema de pagamentos 1.0\n')

# Formas de pagamento e descontos
pv_pc = 0.10
vc = 0.05
c_3x = 0.20


try:
    preço = float(input('Por favor insira o valor do produto: R$ '))

    print('\nEscolha uma das opções de pagamento:\n')                       
    print('1 - Pagamento à vista [Dinheiro/PIX/Cheque].\n'
        '2 - Pagamento à vista no cartão.\n'
        '3 - Parcelado até 2x vezes no cartão.\n'
        '4 - De 3x até 12x vezes no cartão.\n')

    esc = int(input('Opção '))

    if esc == 1:
        print(f'\nPagando à vista você recebe 10% de desconto na sua compra.\nO valor da sua compra de R$ {preço:.2f} fica em R$ {preço - preço * pv_pc:.2f}.\n')
    elif esc == 2:
        print(f'\nPagando à vista no cartão você recebe 5% de desconto.\nO valor da sua compra de R$ {preço:.2f} fica em R$ {preço - preço * vc:.2f}.\n')
    elif esc == 3:
        print(f'\nParcelando em até 2 vezes de R$ {preço / 2:.2f} você não recebe desconto\npermanecendo no valor final de R$ {preço:.2f}.\n')
    elif esc == 4:
        parc = int(input("Deseja parcelar em quantas parcelas?: "))
        print(f'\nParcelando em {parc} de R$ {(preço * c_3x + preço) / parc:.2f} vezes você tera 20% de juros encima da compra.'
        f'\nO valor da sua compra de R$ {preço:.2f} ficará em R$ {preço * c_3x + preço:.2f}.\n')
    else:
        print('\n\033[1;31m[Erro] Opção inválida\n\033[m')

except ValueError:
        print('\n\033[1;31m[Erro] Digite somente números.\n\033[m')
