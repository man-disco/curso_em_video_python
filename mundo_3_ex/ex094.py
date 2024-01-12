# dicionário de pessoas
pessoa = {}
grupo = []
mulheres = []
acima_da_media = []
media = 0
print('\033[1mSistema de pessoas 9000\033[m')
while True:
    pessoa['nome'] = str(input('\nNome: ').strip().title())
    pessoa['idade'] = int(input('Idade: '))
    media += pessoa['idade']
    pessoa['sexo'] = str(input('Sexo [M/F]: ').strip().upper())
    while 'M' != pessoa['sexo'] and 'F' != pessoa['sexo']:
        print('\033[33mTente um sexo válido -> M ou F!\033[m\n')
        pessoa['sexo'] = str(input('Sexo [M/F]: ').strip().upper())
    grupo.append(pessoa.copy())
    cont = str(input('\nDeseja continuar? [S/n]: ').strip().lower())
    while cont != 's' and cont != 'n' and cont != '':
        print('\033[31mEscolha S ou N!\033[m')
        cont = str(input('\nDeseja continuar? [S/n]: ').strip().lower())
        continue
    if cont == 's' or cont == '':
        continue
    else:
        break
media //= len(grupo)
print('-'*30, end='\n')
if len(grupo) > 1:
    print(f'A) O grupo tem {len(grupo)} pessoas.')
else:
    print('A) O grupo tem apenas uma pessoa.')
for p, pd in enumerate(grupo):
    for key, val in pd.items():
        if key == 'sexo' and val == 'F':
            mulheres.append(pd['nome'][:])
        if key == 'idade':
            if val >= media:
                acima_da_media.append(pd.copy())
print(f'B) A média de idade no grupo é de {media} anos.')
if len(mulheres) > 0:
    print(f'C) As mulheres cadastradas foram {", ".join(mulheres)}.')
else:
    print('C) Não houveram mulheres cadastradas.')
print(f'D) Pessoas acima da média do grupo:')
print('-'*30)
for adm in acima_da_media:
    for k, v in adm.items():
        print(f'|{str(k) + " → " + str(v):^28}|')
print('-'*30)
for gp in grupo:
    print(gp)
    
