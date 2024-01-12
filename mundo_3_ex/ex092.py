from datetime import datetime
# sistema de carteira de trabalho]


CURRENT_YEAR = datetime.now().year
cadastro = dict()
cadastro['Nome'] = str(input('Nome: ').strip().capitalize())
cadastro['Idade'] = CURRENT_YEAR - int(input('Ano de nascimento: '))
cadastro['CTPS'] = int(input('Contratos na carteira (0 para pular): '))
if cadastro['CTPS'] > 0:
    cadastro['Empresa'] = str(input('Empresa: ').strip().title())
    cadastro['Ano_contratação'] = int(input('Ano de contratação: '))
    cadastro['Salário'] = float(input('Salário: '))
    aposentadoria = 35 - (CURRENT_YEAR - cadastro['Ano_contratação'])
    print(f'\nFaltam {aposentadoria} anos para esse '
          'funcionário se aposentar! '
          f'({aposentadoria + cadastro["Idade"]} anos)')
for key, val in cadastro.items():
    print(f'{"-"*30}\n{key + " -> "  + str(val):^30}')
print('-'*30)
