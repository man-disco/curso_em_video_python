# Média entre pessoas
soma_idade = 0
média_idade = 0

homem_mais_velho = ''
idade_homem_mais_velho = 0

mulheres_20_anos = 0
mulheres_20_anos_lista = []

print('\n ~~~ Sistema de média social 1.0 ~~~\n')

try:
    for i in range(1, 5):
        print('------ Nome da {}ª pessoa: ------'.format(i))
        nome = input('Nome: ').title().strip()
        idade = int(input('Idade da pessoa: '))
        sexo = input('Sexo da pessoa (M/F): ').strip()

        
        # Checa o valor do sexo da pessoa e se não for "m" ou "f" para o programa
        if sexo in "Mm":
            pass
        elif sexo in "Ff":
            pass
        else:
            print('\n\033[33mEscolha um sexo válido\033[m')
            exit()
            

        # Checa qual é o homem mais velho do loop
        if i == 1 and sexo in 'Mm':
            idade_homem_mais_velho = idade
            homem_mais_velho = nome

        if sexo in "Mm" and idade > idade_homem_mais_velho:
            idade_homem_mais_velho = idade
            homem_mais_velho = nome

        # Checa quantas mulheres tem menos de 20 anos
        if sexo in 'Ff' and idade < 20:
            mulheres_20_anos_lista.append(nome)
            mulheres_20_anos += 1

        soma_idade += idade

    média_idade = soma_idade / i

    # print('\nA soma de todas as idades é de {:.2f} anos.'.format(soma))
    print('\nA média de todas as idades é de {:.2f} anos.'.format(média_idade))
    print('\nO homem mais velho do grupo é {} com {} anos.'.format(homem_mais_velho, idade_homem_mais_velho))

    if mulheres_20_anos > 0:
        print('\nO total de mulheres menores de 20 anos é {}, que são: {}.'.format(mulheres_20_anos, mulheres_20_anos_lista))
    else:
        print('\nNão houve mulheres menores de 20 anos.')

except ValueError:
    print("\n\033[31mDigite apenas valores válidos.\033[m")