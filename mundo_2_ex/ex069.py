# Registro de pessoas
homens = maiores_18 = mulheres_20_anos = 0
nomes = []
continuar = 's'
line = 40 * '-'
while continuar == 's':
    print('----------Sistema De Cadastro----------')
    nome = str(input('Nome: ')).strip().capitalize()
    nomes.append(nome)

    idade = int(input('Idade: '))
    sexo = str(input('Sexo (F/M): ')).strip().lower()
    if sexo in 'Mm':
        sexo = 'M'
        homens += 1
    elif sexo in 'Ff':
        sexo = 'F'
    else:
        break
    while sexo not in 'MmFf':
        print('\033[33mErro! Digite um sexo válido!\033[m\n')
        sexo = str(input('Sexo (F/M): ')).strip().lower()

    if idade >= 18:
        maiores_18 += 1
    if idade > 20 and sexo == 'F':
        mulheres_20_anos += 1
    
    continuar = str(input('Deseja continuar? (S/N): ')).strip().lower()
    while continuar != 's' and continuar != 'n':
        print('\033[33mErro! Digite S ou N\033[m\n')
        continuar = str(input('Deseja continuar? (S/N): ')).strip().lower()

    if continuar == 's':
        continue
    else:
        print('Saindo...\n')
     
    print(f'{line}\n{"Dados":^40}\n{line}')
    print(f'Pessoas maiores de 18: {maiores_18}\n{line}\n'
          f'Mulheres maiores de 20 anos: {mulheres_20_anos}\n{line}\n'
          f'Quantidade de homens cadastrados: {homens}\n{line}\n'
          f'Nomes de pessoas cadastradas:\n{", ".join(nomes)}\n{line}')
