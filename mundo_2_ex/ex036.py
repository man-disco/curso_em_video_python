# Aprovação de empréstimo bancário

valor_emprestimo = float(input('\nQual é o valor do imóvel? R$ '))
salario_comprador = float(input('Qual é valor do seu salário atual? R$ '))
anos_parc = int(input('Qual é o prazo anual desejado para o seu pagamento? '))

prestação_mensal = valor_emprestimo / (anos_parc * 12) 


print(f'\n{anos_parc * 12} meses ({anos_parc} anos) calculam o valor mensal de R$ {prestação_mensal:.2f} por parcela.')

if prestação_mensal > (salario_comprador * 0.30):
    print(f'\n\033[33m30% do salário do cliente resulta em R$ {salario_comprador * 0.30:.2f}, que é um valor inferior a parcela mensal de R$ {prestação_mensal:.2f}.\033[m')
    print(f'\033[31mSegundo a análise do crédito o seu emprestimo foi NEGADO.\033[m')

else:
    print('\033[32mSeu empréstimo foi APROVADO.\033[m')
