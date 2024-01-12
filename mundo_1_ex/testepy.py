def info_prod(prod, prod_id, valor_cartão, valor_pix):
    prod = prod
    prod_id = prod_id
    valor_cartão = valor_cartão
    valor_pix = valor_pix
    desc = valor_cartão - valor_pix

    print(f'\n\033[1m{prod}\033[m\n{"-" * len(prod)}\n'
    f'id: {prod_id}\n'
    f'Valor no cartão em até 12x: R${valor_cartão:.2f}\n'
    f'Valor no pix: R${valor_pix:.2f}\n'
    f'Total do desconto: R${desc:.2f}\n'
    f'Percentual do desconto: {(desc / valor_cartão) * 100:.0f}%\n')

prod = input('insira o nome produto: ')
prod_id = input('Insira o id do produto: ')
valor_cartão = float(input('Insira o valor total parcelado: '))
valor_pix = float(input('Insira o valor com desconto no pix: '))

info_prod(prod, prod_id, valor_cartão, valor_pix)
