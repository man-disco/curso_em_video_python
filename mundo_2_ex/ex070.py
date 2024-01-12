# Sistema de produtos
continuar = True
valor_final = mais_de_1000 = valor_mais_barato = 0

print('-'*35 + f'\n{"Suas compras:":^35}\n' + '-' * 35)
while continuar == True:
    nome_produto = str(input('Nome do produto: ')).strip().lower()
    valor_produto = float(input('Valor do produto: R$ '))
    if valor_produto <= 0:
        print('Erro! Digite um valor válido!')
        continue
    valor_mais_barato = valor_produto
    mais_barato = nome_produto
    if valor_produto < valor_mais_barato:
        valor_mais_barato = valor_produto
        mais_barato = nome_produto
    if valor_produto > 1000:
        mais_de_1000 += 1
    valor_final += valor_produto

    continuar_programa = str(input('Deseja continuar? (s/n): ')).strip().lower()
    while continuar_programa != 's' and continuar_programa != 'n':
        print('\033[33mDigite uma opção válida\033[m')
        continuar_programa = str(input('Deseja continuar? (s/n): ')).strip().lower()
    if continuar_programa == 's':
        pass
    else:
        continuar = False

print(f'O produto mais barato é o "{mais_barato}", que custa R$ {valor_mais_barato:.2f}.')
print(f'Existem {mais_de_1000} produtos com o valor acima de R$ 1000.')
print(f'\nO total da sua compra foi R$ {valor_final:.2f}.')



