# Validação de dados
print('\nSistema de Cadastro Único\n')

nome = input('Nome de usuário: ').strip().title()
nome = nome.split()

sexo = str(input('Sexo do usuário [M/F]: ')).strip().upper()[0]

while sexo not in 'MmFf':
    print('Digite um sexo válido!')
    sexo = str(input('Sexo do usuário [M/F]: ')).strip().upper()[0]

idade = int(input('Idade: '))

print('\n\033[32mCadastro criado com sucesso!\033[m\n')
print('-' * 25)

if sexo in 'M':
    print(f'{"":^2}Seja bem vindo {nome[0]}!')
else:
    print(f'{"":^2}Seja bem vinda {nome[0]}!')

print('-' * 25)
# print('{:^2}'.format('Seus dados'))
print('{:^24}\n{}\nSexo: {:^4} |  Idade: {:^4}'.format(' Seus dados:', '-' * 25, sexo, idade))
print('-' * 25)