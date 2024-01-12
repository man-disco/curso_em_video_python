# Lista de produtos
lista = ('Arroz Patinho', 22.95, 'Feijão Bonitto', 10.99, 'Macarrão', 12.00, 'Pera', 8.99, 'Picanha', 13.99)

print( '-' * 50 + f'\n\033[1m{"Mercado Bão Dimais Só":^50}\033[m\n' + '-' * 50 )
for prod in lista:
    if lista.index(prod) % 2 == 0:
            print(f'{prod:.<42}', end='R$ ')
    else:
        print(f'{prod:>5.2f}')
print('-' * 50)
