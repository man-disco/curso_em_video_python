# Matriz 3x3 aprimorada
mat = []
col = []
num_col = soma_par = soma_col3 = maior_col2 = 0
while len(mat) < 3:
    while len(col) < 3:
        col.append(int(input(f'coord {len(col)}, {num_col} ')))
    num_col += 1
    mat.append(col[:])
    col.clear()

print('\nMatriz Gerada\n')
for pos, lin in enumerate(mat):
    print(pos, end=' ')
    for num in lin:
            print(f'[{num:^5}]', end='')
            if pos == 2:
                if num == lin[0]:
                    maior_col2 = num
                if num > maior_col2:
                    maior_col2 = num
            # Soma os valores da linha 1
            if pos == 2:
                soma_col3 += num
            # Soma os valores pares
            if num % 2 == 0:
                soma_par += num
    print('\n', end='')

print(f'\nA soma dos valores pares resultam em: {soma_par}')
print(f'A soma dos valores da coluna 3 resultam em: {soma_col3}')
print(f'O maior valor da coluna 2 é {maior_col2}')
